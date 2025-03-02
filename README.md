# Curve Fitting and Least Squares Approximation

## Overview
This project implements various mathematical functions to approximate given data points using the **Least Squares Method**. The program determines the best-fitting function based on the deviation measure and root mean square deviation.

## Features
- Supports multiple function types:
  - **Linear function**: \( \varphi(x) = ax + b \)
  - **Quadratic function**: \( \varphi(x) = ax^2 + bx + c \)
  - **Cubic function**: \( \varphi(x) = ax^3 + bx^2 + cx + d \)
  - **Exponential function**: \( \varphi(x) = a \cdot b^x \)
  - **Logarithmic function**: \( \varphi(x) = a \cdot \log_b(x) \)
  - **Power function**: \( \varphi(x) = a \cdot x^b \)
- Uses the **Least Squares Method** to determine the optimal coefficients.
- Calculates **total deviation** and **root mean square deviation**.
- Reads data from a text file and determines the best-fitting function.
- Plots the original data points and the fitted function graphically.

## Installation
### Prerequisites
Make sure you have **Python 3.x** installed along with the required dependencies:

```bash
pip install numpy matplotlib
```

## Usage
1. Prepare a data file (`data.txt`) with values in the format:
   ```
   x1,y1
   x2,y2
   ...
   ```
2. Run the script:
   ```bash
   python main.py
   ```
3. The program will output:
   - The best-fitting function.
   - Its coefficients.
   - Deviation measures.
   - A graphical representation of the best function.

## Example Output
```
Наиболее точная функция: Полиномиальная 2-й степени: ϕ(x) = ax² + bx + c
Коэффициенты: [2.5, -1.2, 0.8]
Мера отклонения (S): 0.034

Результаты для всех функций:
...
```

## Graphical Representation
The program generates a plot where:
- **Blue dots** represent the original data points.
- **Red line** represents the best-fitting function.

## License
This project is open-source and licensed under the **MIT License**.

## Author
Developed by [KatyaZubareva] 🚀

