from app.chat_gpt import work_exp_auto, api_key
import os

from app.resume_gen import job_listing

email = 'dendvnk@proton.me'
pswd = '=rNEHr:L#*W8e*m'
name = 'Den'
photo_path = os.path.abspath(os.getcwd()) + '/images/412e01d3-9af4-45f9-8cdd-483716b2f778.jpg'
university = 'Harvard University'
degree = "Bachelor's degree"
spec = 'Web design'
age = '27'
grade = '95'
position = 'Web Developer'
company_name = 'MAANG INTERNATIONAL'
company_geo = 'Telangana'
industry = 'Software Development'
pos_desc = 'Senior developer'
short_desc = 'Harvard graduate, web developer at MAANG'
skills_lst = ['Python', 'Django', 'Selenium', 'REST', 'Celery', 'Docker', 'SQL']
desc_for_work_exp = [f'My name is {name}', f'{age} years old', 'Google', f'Graduated from {university}',
                'working from 01.08.2019 to 25.12.2022', 'web design', 'python', 'programming', 'selenium', 'Django']
if len(api_key) > 0:
    try:
        work_experience = work_exp_auto(desc_for_work_exp, api_key)['choices'][0]['text']
    except:
        Exception('Your api is wrong, for work_experience I will use Faker')
        work_experience = job_listing()
else:
    print('Your api is wrong, for work_experience I will use Faker')
    work_experience = job_listing()