import React, { Component } from "react";
import { render } from "react-dom";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import AdminDashboard from "./AdminDashboard";
import Registration from "./Registration";
import LoginPage from "./LoginPage";


export default class App extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return ( 
      <Router>
        <Routes>
          <Route path='/login' element={<AdminDashboard />}/>
          <Route path='/register-nurse' element={<Registration />}/>
          <Route path='/' element={<LoginPage />}/>
        </Routes>
      </Router>
    );
  }
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);