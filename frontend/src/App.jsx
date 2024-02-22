import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Landing from "./pages/Landing.jsx";

export default function App() {
  return (
    <div className="">
      <Router>
          <Routes>
            <Route path="/" element={<Landing />} />
          </Routes>
      </Router>
    </div>
  );
}
  
  