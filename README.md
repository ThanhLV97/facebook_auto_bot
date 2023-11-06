# Selenium Python Automation

Facebook auto bot for posting into public group

## WARNING: This repo is designed to support business purposes. Any illegal use will be met with strict consequences, and users must fully assume responsibility.

## Updated at: 06/11/2023

Note: All selectors or XPaths could be changed in the future. Please create an issue if you encounter any problems.

## Setup

1. Clone this repository

```bash
git clone https://github.com/ThanhLV97/facebook_auto_bot.git
```

2. Access into project's folder

```bash
cd facebook_auto_bot
```

3. Create a virtual environment

```bash
python3 -m venv venv
```

4. Activate the environment

```bash
source venv/bin/activate
```

5. Create a .env file
```bash
touch .env
```

6. Add the following lines to .env:

```
EMAIL=your_email@example.com
PASSWORD=your_password
```

7. Install dependencies from requirements.txt

```bash
pip install -r requirements.txt
```

requirements.txt contains:

```
selenium==4.15.2
python-dotenv==1.0.0
pandas==2.1.2
```

8. Custome photos and status for your post:
   `Upload photos into data/image folder and status in status.txt file. Add your group link in the group.csv file`
9. Run the script

```bash
python main.py
```

Let me know if you need any clarification or have additional questions!
