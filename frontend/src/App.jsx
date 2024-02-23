import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Landing from "./pages/Landing.jsx";
import Login from "./pages/Login.jsx";
import Signup from "./pages/Signup.jsx";

export default function App() {
  return (
    <div className="">
      <Router>
          <Routes>
            <Route path="/" element={<Landing />} />
            <Route path="/login" element={<Login/>} />
            <Route path="/signup" element={<Signup/>}/>
          </Routes>
      </Router>
    </div>
  );
}
  
  