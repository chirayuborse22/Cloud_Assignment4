from flask import Flask

app = Flask(__name__)

@app.route('/')
def scientific_calculator():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Scientific Calculator</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                margin-top: 50px;
                background-color: #f4f4f9;
                color: #333;
            }
            input, button {
                width: 80px;
                height: 40px;
                font-size: 16px;
                margin: 5px;
                border-radius: 5px;
                border: 1px solid #ccc;
            }
            button {
                background-color: #007BFF;
                color: white;
                cursor: pointer;
            }
            button:hover {
                background-color: #0056b3;
            }
            #result {
                width: 200px;
                height: 40px;
                font-size: 18px;
                margin-top: 15px;
                border: 2px solid #007BFF;
                border-radius: 5px;
                background-color: #f1f1f1;
                text-align: center;
            }
            .container {
                display: inline-block;
                padding: 20px;
                background: white;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
                border-radius: 10px;
            }
            .row {
                margin-bottom: 10px;
            }
            .number-row {
                display: flex;
                justify-content: center;
            }
            .number-row button {
                width: 60px;
            }
            @media (max-width: 500px) {
                input, button, #result {
                    width: 100px;
                    height: 40px;
                    font-size: 14px;
                }
            }
        </style>
    </head>
    <body>
        <h1>Scientific Calculator</h1>
        <div class="container">
            <div class="row">
                <input type="text" id="num1" placeholder="Enter number 1">
            </div>
            <div class="row">
                <input type="text" id="num2" placeholder="Enter number 2">
            </div>
           
            <div class="number-row">
                <button onclick="addNumber(0, 'num1')">0</button>
                <button onclick="clearInput()">C</button>
                <button onclick="calculate('+')">+</button>
            </div>
            <div class="number-row">
                <button onclick="addNumber(1, 'num2')">1</button>
                <button onclick="addNumber(2, 'num2')">2</button>
                <button onclick="addNumber(3, 'num2')">3</button>
            </div>
            <div class="number-row">
                <button onclick="addNumber(4, 'num2')">4</button>
                <button onclick="addNumber(5, 'num2')">5</button>
                <button onclick="addNumber(6, 'num2')">6</button>
            </div>
            <div class="number-row">
                <button onclick="addNumber(7, 'num2')">7</button>
                <button onclick="addNumber(8, 'num2')">8</button>
                <button onclick="addNumber(9, 'num2')">9</button>
            </div>
            <div class="number-row">
                <button onclick="addNumber(0, 'num2')">0</button>
                <button onclick="clearInput()">C</button>
                <button onclick="calculate('-')">-</button>
            </div>
            <div class="row">
                <button onclick="calculate('*')">*</button>
                <button onclick="calculate('/')">/</button>
                <button onclick="calculate('sqrt')">√</button>
                <button onclick="calculate('^')">^</button>
            </div>
            <div class="row">
                <button onclick="calculate('sin')">sin</button>
                <button onclick="calculate('cos')">cos</button>
                <button onclick="calculate('tan')">tan</button>
                <button onclick="calculate('log')">log</button>
                <button onclick="calculate('!')">n!</button>
            </div>
            <div class="row">
                <input type="text" id="result" readonly placeholder="Result">
            </div>
        </div>
        <script>
            function factorial(n) {
                if (n < 0) return 'Undefined';
                if (n === 0 || n === 1) return 1;
                let result = 1;
                for (let i = 2; i <= n; i++) {
                    result *= i;
                }
                return result;
            }

            function calculate(op) {
                const num1 = parseFloat(document.getElementById('num1').value);
                const num2 = parseFloat(document.getElementById('num2').value);
                let result;
                
                if (isNaN(num1) && (op !== '!' && op !== 'sqrt')) {
                    result = 'Enter valid input';
                } else {
                    switch(op) {
                        case '+': result = num1 + num2; break;
                        case '-': result = num1 - num2; break;
                        case '*': result = num1 * num2; break;
                        case '/': 
                            result = num2 === 0 ? 'Cannot divide by zero' : num1 / num2;
                            break;
                        case 'sqrt': 
                            result = num1 < 0 ? 'Invalid Input' : Math.sqrt(num1);
                            break;
                        case '^': result = Math.pow(num1, num2); break;
                        case 'log': 
                            result = num1 <= 0 ? 'Invalid Input' : Math.log10(num1);
                            break;
                        case '!': result = factorial(num1); break;
                        case 'sin': result = Math.sin(num1 * Math.PI / 180); break;
                        case 'cos': result = Math.cos(num1 * Math.PI / 180); break;
                        case 'tan': result = Math.tan(num1 * Math.PI / 180); break;
                        default: result = 'Unknown operation';
                    }
                }
                document.getElementById('result').value = result;
            }

            function addNumber(number, inputField) {
                const currentValue = document.getElementById(inputField).value;
                document.getElementById(inputField).value = currentValue + number;
            }

            function clearInput() {
                document.getElementById('num1').value = '';
                document.getElementById('num2').value = '';
                document.getElementById('result').value = '';
            }
        </script>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
