import React, { Component } from "react";
import Select from '@mui/material/Select';
import Button from "@mui/material/Button";
import Grid from "@mui/material/Grid";
import TextField from "@mui/material/TextField";
import FormControl from '@mui/material/FormControl'
import MenuItem from '@mui/material/MenuItem';
import InputLabel from '@mui/material/InputLabel';
import Box from '@mui/material/Box';
import Typography from "@mui/material/Typography";
import { Link } from "react-router-dom";

export default class LoginPage extends Component {
  constructor(props) {
    super(props);

    // Initialize the state
    this.state = {
      user_type: '',
    };
  }

  handleChange = (e) => {
    // Update the state when the selection changes
    this.setState({ user_type: e.target.value });
  };

  render() {
    const { user_type } = this.state;
    return (
      <Grid container spacing={1}>
        <Grid item xs={12} align="center">
          <Typography component="h4" variant="h4">
            LOGIN
          </Typography>
          </Grid>
        <Grid item xs={12} align="center">
          <Box sx={{ minWidth: 120 }}>
            <FormControl style={{ width: '200px' }}>
              <InputLabel id="selected_type">UserType</InputLabel>
              <Select
              labelId="Choose Type"
              id="select-user"
              value={user_type}
              label="choose type"
              onChange={this.handleChange}
              inputProps={{ 'aria-label': 'Without label' }}>
                <MenuItem value={"admin"}>Admin</MenuItem>
                <MenuItem value={"nurse"}>Nurse</MenuItem>
                <MenuItem value={"patient"}>Patient</MenuItem>
              </Select>
            </FormControl>
          </Box>
        </Grid>
        <Grid item xs={12} align="center">
          <TextField id="username" label="Username" type="search" />
        </Grid>
        <Grid item xs={12} align="center">
          <TextField
            id="pw"
            label="Password"
            type="password"
            autoComplete="current-password"
          />
        </Grid>
        <Grid item xs={12} align="center">
          <Button variant="contained" to="/login " component={Link}>
            Login
          </Button>
        </Grid>
      </Grid>
    );
  }
}
