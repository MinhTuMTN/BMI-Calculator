// Import css
import { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [weight, setWeight] = useState(60);
  const [height, setHeight] = useState(170);
  const [bmi, setBmi] = useState(0);
  const [result, setResult] = useState("");

  const calculateBMI = (weight, height) => {
    let bmi = weight / (height / 100) ** 2;
    return bmi.toFixed(2);
  };

  const displayResult = (bmi) => {
    let result = "";
    if (bmi < 18.5) {
      result = "Underweight";
    } else if (bmi < 25) {
      result = "Normal";
    } else if (bmi < 30) {
      result = "Overweight";
    } else {
      result = "Obese";
    }
    return result;
  };

  useEffect(() => {
    setBmi(calculateBMI(weight, height));
    setResult(displayResult(bmi));
  }, [weight, height, bmi]);

  // Code return layout for bmi calculator
  return (
    <div className="container">
      <div className="App">
        <h1>BMI Calculator</h1>
        <form>
          <label htmlFor="weight">Weight(kg):</label>
          <input
            type="number"
            id="weight"
            name="weight"
            value={weight}
            onChange={(e) => setWeight(e.target.value)}
          />
          <br />
          <label htmlFor="height">Height(cm):</label>
          <input
            type="number"
            id="height"
            name="height"
            value={height}
            onChange={(e) => setHeight(e.target.value)}
          />
          <br />
        </form>
        <div id="result">
          <div>Your BMI is {bmi}</div>
          <div>You are {result}</div>
        </div>
      </div>
    </div>
  );
}

export default App;
