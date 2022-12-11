import React, { useEffect, useState } from "react";
import TextField from "@mui/material/TextField";
import FormControl from "@mui/material/FormControl";
import { Button } from "@mui/material";
import "../App.css";

function Home() {
  const [query, setQuery] = useState("");
  const Submit = (e) => {
    e.preventDefault();
    console.log(query);
    fetch("http://127.0.0.1:5000/main", {
      method: "POST",
      mode: "no-cors",
      headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
      },
      body: JSON.stringify(query),
    })
      .then((data) => {
        data.json();
        console.log(data);
      })
      .then((data) => {
        if (data.code == 200) {
        } else {
          alert(data.error);
        }
      })
      .then(alert("Success!"))
      .catch((error) => console.error(error));
  };

  return (
    <div className="container">
      <h1 className="main-header">Research Assistant</h1>
      <FormControl sx={{ m: 1, width: 300 }}>
        <TextField
          required
          id="filled-required"
          label="Query"
          variant="filled"
          value={query}
          onChange={(e) => {
            setQuery(e.target.value);
          }}
        />
        <Button type="submit" onClick={Submit}>
          Submit
        </Button>
      </FormControl>
    </div>
  );
}

export default Home;
