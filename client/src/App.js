import React, { useEffect, useState, useRef } from "react";
import "./App.css";

/** @jsx jsx */
import { jsx } from "@emotion/core";
import { ViewCount, Button, Title, Section } from "./styled";

function usePrevious(value) {
  const ref = useRef();
  useEffect(() => {
    ref.current = value;
  });
  return ref.current;
}

function App() {
  let [count, setCount] = useState(0);
  const prevAmount = usePrevious({ count, setCount });
  useEffect(() => {
    getCount();
  }, []);

  function getCount() {
    fetch("http://localhost:5000/api/item", {
      headers: {
        'counter-increment': 1
      }
    })
      .then((response) => response.json())
      .then((body) => {
        setCount(body.count)
      });
  }

  return (
    <div className="App">
      <Section>
        <Title>Total Count:</Title>
        <ViewCount>{count}</ViewCount>
        <Button onClick={() => setCount(count + 1)}>+1</Button>
        <Button onClick={() => setCount(count + 100)}>+100</Button>
      </Section>
    </div>
  );
}

export default App;
