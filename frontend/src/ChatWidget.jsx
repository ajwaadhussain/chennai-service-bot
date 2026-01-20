import { useState } from "react";
import "./ChatWidget.css";

export default function ChatWidget() {
  const [open, setOpen] = useState(false);
  const [msgs, setMsgs] = useState([
    { role: "bot", text: "Hello! I am your Chennai Guide. Ask me about hospitals, buses, or utilities!" },
  ]);
  const [text, setText] = useState("");
  const [loading, setLoading] = useState(false);

  async function send() {
    const msg = text.trim();
    if (!msg) return;

    // 1. Add user message to screen
    setMsgs((m) => [...m, { role: "user", text: msg }]);
    setText("");
    setLoading(true);

    try {
      // 2. Send to Backend
      const res = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: msg }),
      });

      const data = await res.json();

      // 3. Add bot answer to screen
      setMsgs((m) => [...m, { role: "bot", text: data.answer }]);
    } catch (err) {
      setMsgs((m) => [...m, { role: "bot", text: "⚠️ Error connecting to server." }]);
    }
    setLoading(false);
  }

  return (
    <>
      {/* Floating Button */}
      <button className="chat-fab" onClick={() => setOpen(!open)}>
        {open ? "✖" : "💬 Help"}
      </button>

      {/* Chat Window */}
      {open && (
        <div className="chat-modal">
          <div className="chat-header">Chennai Service Bot 🤖</div>

          <div className="chat-body">
            {msgs.map((m, i) => (
              <div key={i} className={`bubble ${m.role}`}>
                {m.text}
              </div>
            ))}
            {loading && <div className="bubble bot">Typing...</div>}
          </div>

          <div className="chat-input">
            <input
              value={text}
              onChange={(e) => setText(e.target.value)}
              placeholder="Ask about Chennai services..."
              onKeyDown={(e) => e.key === "Enter" && send()}
            />
            <button onClick={send} disabled={loading}>Send</button>
          </div>
        </div>
      )}
    </>
  );
}