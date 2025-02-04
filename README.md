# Binomial Tree Option Valuation

Otherwise known as CRR valuation, the CRR model, or the Cox-Ross-Rubinstein
market model.

This repository contains a Python implementation of the Binomial Tree Option
valuation, based on its definition Chapter 13 of 'Derivatives Markets' by Robert
L. McDonald. It provides the value of a american or european call or put option,
based on its current stock value, its strike price, the risk free rate, the time
until maturity, volatility, dividend, and number of steps.

The implementation details can be found in the file `/src/main.py`.

## Prerequisites

To run the script, you must have Python installed. For instructions on how to
download Python, consult
[the Python documentation](https://www.python.org/downloads/).

You must also have git installed.

## Running the project

```bash
git clone https://github.com/BendikSolevag/binomial-option-valuation

cd binomial-option-pricing

python ./src/main.py
```
