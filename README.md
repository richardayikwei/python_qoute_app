# 🧾 Quote Display App

A simple Python desktop app that displays a random inspirational quote in a window using the built-in `tkinter` GUI library.

# Update

Included an executable for definition subjects i want to remeber frequently

---

## 📂 About the Project

This app randomly selects a quote from a predefined dictionary and displays it in a neat pop-up window. Great for daily motivation or as a beginner GUI project.

---

## 🚀 Getting Started

### 1. **Fork and Clone the Repository**

```bash
git clone https://github.com/richardayikwei/python_qoute_app.git
cd python_qoute_app
```

### 2. uv install

### 3. Add a quote of your choice in this format into quotes variable

```'Name of author of quote' : 'Quote of the author'
```
Seperate you new entry from the old entries using a comma ","

### 4. Use
``` 
pyinstaller --onefile --noconsole main.py
```
to compile scipt into executable

### 5. ⏰ Automate with Windows Task Scheduler

You can use Windows Task Scheduler to run the app automatically (e.g., every morning, on login, etc.).

### 🔧 Steps to Schedule the Script

#### 1. Open Task Scheduler

- Press `Win + S` and search for **Task Scheduler**
- Open it

#### 2. Create a New Task

- Click **"Create Task..."** in the right-hand panel
- Give your task a name like: `Daily Quote App`

#### 3. Choose Trigger

Choose when you want it to run:
- Daily (e.g., every morning)
- At log on (when you log into your computer)

example of a trigger
![alt text](<Screenshot 2025-07-09 105744.png>)

#### 4. Choose Action: Start a Program

### Notes

1. Keep quotes motivational
2. Remember to change your python interpretor to the uv environment to ensure script compiles 

## 📃 License

This project is licensed under the [CC BY 4.0 License](https://creativecommons.org/licenses/by/4.0/).  
You are free to use, modify, and distribute it — just remember to give credit!