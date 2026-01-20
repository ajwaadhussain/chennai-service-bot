import ChatWidget from "./ChatWidget";

function App() {
  return (
    <div style={{ 
      height: "100vh", 
      display: "flex", 
      flexDirection: "column", 
      justifyContent: "center", 
      alignItems: "center", 
      background: "#282c34", 
      color: "white",
      fontFamily: "sans-serif"
    }}>
      <h1>Welcome to Chennai Services</h1>
      <p>Click the "Help" button below to chat with our AI agent.</p>
      
      {/* This adds the chat bot to the page */}
      <ChatWidget />
    </div>
  );
}

export default App;