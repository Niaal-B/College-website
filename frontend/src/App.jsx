import {
    BrowserRouter as Router,
    Route,
    Routes,
    Navigate,
  } from "react-router-dom";
  import Home from "./pages/Home";
  import Login from "./pages/Login";
  import Dashboard from "./pages/Dashboard";
  import { useState, useEffect } from "react";
  
  const App = () => {
    const [isAuthenticated, setIsAuthenticated] = useState(false);
  
    // Correct way to check the token and set authentication state
    useEffect(() => {
      const token = localStorage.getItem("accessToken");
      setIsAuthenticated(!!token);
    }, []); // Runs only once when the component mounts
  
    return (
      <Router>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login setAuth={setIsAuthenticated} />} />
  
          {/* Protect Dashboard without ProtectedRoute.js */}
          <Route
            path="/dashboard"
            element={isAuthenticated ? <Dashboard /> : <Navigate to="/login" />}
          />
  
          {/* Redirect unknown routes */}
          <Route
            path="*"
            element={<Navigate to={isAuthenticated ? "/dashboard" : "/login"} />}
          />
        </Routes>
      </Router>
    );
  };
  
  export default App;
  