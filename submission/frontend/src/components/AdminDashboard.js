import React, { Component } from "react";
import Button from "@mui/material/Button";
import Grid from "@mui/material/Grid";
import Typography from "@mui/material/Typography";
import TextField from "@mui/material/TextField";
// import FormHelperText from "@mui/material/FormHelperText";
// import FormControl from "@mui/material/FormControl";
import { Link } from "react-router-dom";
// import Radio from "@mmui/material/Radio";
// import RadioGroup from "@mmui/material//RadioGroup";
// import FormControlLabel from "@mui/material/FormControlLabel";

export default class AdminDashboard extends Component {
  constructor(props) {
    super(props);
    this.state = {
      showComponents: false,
      textFieldValue: '',
    };
  }

  handleNurseUpdateClick = () => {
    this.setState({ showNurseUpdateComponents: true });
  };

  handleNurseUpdateTextFieldChange = (e) => {
    this.setState({ NurseUpdatetextFieldValue: e.target.value });
  };

  handleNurseDeleteClick = () => {
    this.setState({ showNurseDeleteComponents: true });
  };

  handleNurseDeleteTextFieldChange = (e) => {
    this.setState({ NurseDeletetextFieldValue: e.target.value });
  };

  handleVaccineUpdateClick = () => {
    this.setState({ showVaccineUpdateComponents: true });
  };

  handleVaccineUpdateTextFieldChange = (e) => {
    this.setState({ VaccineUpdatetextFieldValue: e.target.value });
  };



  render() {
    const { showNurseUpdateComponents, NurseUpdatetextFieldValue, showNurseDeleteComponents, NurseDeletetextFieldValue,
            showVaccineUpdateComponents, VaccineUpdatetextFieldValue} = this.state;
    return(
      <Grid container spacing={1}>
        <Grid item xs={12} align="center">
          <Typography component="h4" variant="h4">
            ADMIN DASHBOARD
          </Typography>
        </Grid>
        <Grid item xs={12} align="center">
            <Button variant="contained" to="/api/add-nurse" component={Link}>
              Register A Nurse
            </Button>
          </Grid>
          <Grid item xs={12} align="center">
            <Button variant="contained" onClick={this.handleNurseUpdateClick}>
              Update Nurse Info
            </Button>
            {showNurseUpdateComponents && (
              <Grid item xs={12} align="center">
                <TextField
                label="Enter Employee ID"
                value={NurseUpdatetextFieldValue}
                type="number"
                onChange={this.handleNurseUpdateTextFieldChange} />
                <Button variant="contained" to={"/api/update-nurse/" + NurseUpdatetextFieldValue + "/"} component={Link}>
                  Submit
                </Button>
              </Grid>)}
          </Grid>
          <Grid item xs={12} align="center">
            <Button variant="contained" onClick={this.handleNurseDeleteClick}>
              Delete a Nurse
            </Button>
            {showNurseDeleteComponents && (
              <Grid item xs={12} align="center">
                <TextField
                label="Enter Employee ID"
                value={NurseDeletetextFieldValue}
                onChange={this.handleNurseDeleteTextFieldChange} />
                <Button variant="contained" to={"/api/del-nurse/" + NurseDeletetextFieldValue + "/"} component={Link}>
                  Submit
                </Button>
              </Grid>)}
          </Grid>
          <Grid item xs={12} align="center">
            <Button variant="contained" to="/api/add-vaccine" component={Link}>
              Add Vaccine
            </Button>
          </Grid>
          <Grid item xs={12} align="center">
            <Button variant="contained" onClick={this.handleVaccineUpdateClick}>
              Update Vaccine
            </Button>
            {showVaccineUpdateComponents && (
              <Grid item xs={12} align="center">
                <TextField
                label="Enter Vaccine ID"
                value={VaccineUpdatetextFieldValue}
                type="number"
                onChange={this.handleVaccineUpdateTextFieldChange} />
                <Button variant="contained" to={"/api/update-vaccine/" + VaccineUpdatetextFieldValue + "/"} component={Link}>
                  Submit
                </Button>
              </Grid>)}
          </Grid>
          <Grid item xs={12} align="center">
            <Button variant="contained" to="/api/nurses" component={Link}>
              View Nurse Info
            </Button>
          </Grid>
          <Grid item xs={12} align="center">
            <Button variant="contained" to="/api/patients" component={Link}>
              View Patient Info
            </Button>
          </Grid>
        </Grid>
      )
  }
}
