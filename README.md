# Gander's Universe Animation Tool

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Creating an Animation](#creating-an-animation)
  - [Adding a Frame](#adding-a-frame)
  - [Listing Animations](#listing-animations)
  - [Retrieving an Animation](#retrieving-an-animation)
- [Database Setup](#database-setup)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Introduction
Gander's Universe is an animation tool designed to create and manage animations with ease. This tool allows users to define animations with multiple frames, store them in a database, and retrieve them for playback or editing.

## Features
- Create animations with multiple frames
- Store animations in a database
- Retrieve and display animations
- Simple command-line interface (CLI) for interaction

## Getting Started

### Prerequisites
- Python 3.6 or higher
- `pip` (Python package installer)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ganders-universe.git
   cd ganders-universe
 2. Install The Required Packages
    ```bash
    pip install -r requirements.txt
  3. Set Up Database
     ```bash
     python src/database/setup.py
