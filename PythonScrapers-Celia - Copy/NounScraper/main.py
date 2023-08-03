import csv
import requests
from bs4 import BeautifulSoup

# Website 1: https://examples.yourdictionary.com/examples-of-skills.html
url1 = "https://examples.yourdictionary.com/examples-of-skills.html"

# Website 2: https://novoresume.com/career-blog/most-important-skills-to-put-on-your-resume
url2 = "https://novoresume.com/career-blog/most-important-skills-to-put-on-your-resume"

# Additional words
additional_words = [
    'Filing', 'Data entry', 'Typing, e.g., 80+ words per minute', 'Zoom scheduling', 'Microsoft Office', 'GSuite',
    'QuickBooks', 'Salesforce', 'Calendar management', 'Presentations', 'First-aid', 'CPR', 'Patience', 'Planning',
    'Imagination', 'Creative activities', 'Scheduling', 'Parental updates', 'Compassion', 'Boundary setting',
    'Thoroughness', 'Safety-first attitude', 'Physical stamina', 'Able to lift 50lbs', 'Reliable', 'Punctual',
    'Efficiency', 'Self-motivation', 'Following instruction', 'Positive attitude', 'Measuring', 'Problem-solving',
    'Machine operation', 'Tool knowledge', 'Safety procedure', 'Reading blueprints', 'Following directions', 'Teamwork',
    'Physical stamina', 'Meeting project deadlines', 'Styling', 'Color treatments', 'Blowouts', 'Client-first attitude',
    'Skin treatments', 'Upselling', 'Product knowledge', 'Attention to detail', 'Rapport building', 'Up-to-date on trends',
    'Empathy', 'Active listening', 'Responsiveness', 'Written communication', 'Verbal communication', 'Sticking to script',
    'Providing solutions', 'Customer retention', 'Friendliness', 'Issue documentation', 'Public speaking',
    'Multimedia learning', 'Inclusiveness', 'Group activities', 'Syllabus creation', 'Lesson planning',
    'Curriculum adherence', 'Test-score improvement', 'Productive assignment', 'Mentorship', 'Event planning',
    'Crowd engagement', 'Sales', 'Writing', 'Promotion', 'Production', 'Social media content', 'Media generation',
    'A/V setup', 'Sound coordination', 'Planning', 'Coordination', 'Timing', 'A/V logistics', 'Client rapport',
    'Networking', 'Sound engineering', 'Scheduling', 'Cross-functional collaboration', 'Off-site events',
    'Health code compliance', 'Strict quality standards', 'Food knowledge', 'Trained palette', 'Knife technique',
    'Reliability', 'Self-motivation', 'Mise en place', 'Cost reduction', 'Ordering', 'Guest-first attitude',
    'Adhering to service standards', 'Attention to detail', 'Natural conversation', 'Physical stamina',
    'Calm under pressure', 'Executing requests', 'Conflict resolution', 'Promptness', 'Recommendations', 'Commitment',
    'Survey creation', 'Payroll coordination', 'Internal emails', 'Presentation', 'Policy knowledge', 'Feedback',
    'Empathy', 'Active listening', 'Price comparison', 'Event organization', 'Conflict resolution', 'Project management',
    'Product research', 'Network maintenance', 'Computer installation', 'Debugging', 'Cloud management', 'Ticket response',
    'Corporate licensing', 'UX', 'Budget monitoring', 'Machine learning', 'Repairs', 'Scheduled upkeep', 'Problem-solving',
    'Machine knowledge', 'Prompt response', 'General fixes', 'Lawn care', 'Yardwork', 'Plumbing', 'Electrical', 'Carpentry',
    'Taking vitals', 'Patient assessment', 'Compassion', 'Reading charts', 'Record keeping', 'Organization',
    'Medicine administration', 'Preparing tools and instruments', 'Modern health code protocol',
    'Use of MRI, X-ray or CAT Scans', 'Glucose monitoring', 'Customer service', 'Product awareness', 'Cash handling',
    'Payment processing', 'Upselling', 'Brand focus', 'Teamwork', 'Loyalty building', 'Clear communication',
    'Promotional help', 'Video monitoring', 'Threat surveillance', 'Crowd control', 'De-escalation', 'Loss prevention',
    'System installation', 'General safety', 'Team coordination', 'Clear communication', 'Integrity', 'Persuasion',
    'Negotiation', 'Persistence', 'Meeting set quotas', 'Attaining growth', 'Building client rapport', 'Exceeding benchmarks',
    'Messaging', 'Product knowledge', 'Passion', 'Marketing/advertising', 'Documenting cases', 'Accessibility',
    'Proactive solutions', 'Counseling', 'Creating', 'Sociability', 'Digital community outreach', 'Results-driven',
    'Working with children', 'Training', 'Lesson planning', 'Curriculum development', 'Classroom management',
    'Student growth', 'Achieving test benchmarks', 'Professionalism', 'Multimedia presentation', 'Cultural awareness',
    'Evoking enthusiasm'
]


response1 = requests.get(url1)                  # Send a GET request to Website 1
soup1 = BeautifulSoup(response1.content, 'html.parser')
li_elements1 = soup1.find_all('li')


response2 = requests.get(url2)                  # Send a GET request to Website 2
soup2 = BeautifulSoup(response2.content, 'html.parser')
li_elements2 = soup2.find_all('li')

words1 = []                         # Extract the words from Website 1 (excluding italicized words and those with more than three words)
for li in li_elements1:
    if not li.find('em'):
        word = li.get_text(strip=True)
        if len(word.split()) <= 3:
            words1.append(word)

words2 = []                         # Extract the words from Website 2 (excluding italicized words and those with more than three words)
for li in li_elements2:
    if not li.find('em'):
        word = li.get_text(strip=True)
        if len(word.split()) <= 3:
            words2.append(word)

# Save all the words to the CSV file
with open('extracted_words.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Additional Words'])
    writer.writerows([[word] for word in additional_words])
    writer.writerow(['Website 1 Words'])
    writer.writerows([[word] for word in words1])
    writer.writerow(['Website 2 Words'])
    writer.writerows([[word] for word in words2])

print("Words saved to 'extracted_words.csv' file.")
