from gtts import gTTS #pip install gTTS
from playsound import playsound #pip install playsound
from os import path


def getLanguage(string): 

  string = string.lower()
  croatian = ['hrvatski', 'hr', 'h', 'cro', 'cr', 'croatian', 'c']
  english = ['engleski', 'en', 'e', 'english']

  if string == '' or (string not in croatian and string not in english):
    return False
  else:
    if string in english:
      return 'english'
    elif string in croatian:
      return 'hrvatski'
      

def createSoundFile(filename, text, language, output=True):
  
  tts = gTTS(text, lang=str(language))
  tts.save(path.curdir + '/' + filename + '.mp3')

  if output == True:
    return  str(path.curdir + '/' + filename + '.mp3')


def checkInput(string):

  string = string.lower()
  positive_input = ['y', 'yes', 'da', 'y', 'd']
  negative_input = ['n', 'no', 'ne']

  if string in positive_input:
    return True
  elif string in negative_input:
    return False
  else:
    return False


def doMaths(string):

  return str(eval(string, {'__builtins__': None}))
 
    
#MAIN LOOP====================================================================
if __name__ == '__main__':

  selected_language = {
    'english': {
      'greeting': 'Welcome, I\'m the Mathematician.',
      'manual_prompt': 'Do you want to listen to the instructions?',
      'manual': 'I am here to answer your maths problems. I can do addition, subtraction, multiplication and division. If there\'s any problem containing those operators, I can solve it!',
      'math_query': 'What\'s your problem',
      'math_query_empty': 'You didn\'t enter a maths problem.',
      'math_query_prompt': 'Is this how you imagined your query? ',
      'math_query_answer': 'The answer is ',
      'goodbye': 'Bye'
    },

    'hrvatski': {
      'greeting': 'Dobrodošli, ja sam Matematičar.',
      'manual_prompt': 'Želite li poslušati upute?',
      'manual': 'Ovdje sam da riješim tvoje probleme s matematikom. Mogu zbrajat, oduzimat, množit i dijelit. Ako postoji bilo koji problem sa tim operatorima, mogu ga riješiti!',
      'math_query': 'Reci mi zadatak.',
      'math_query_empty': 'Niste mi zadali zadatak.',
      'math_query_prompt': 'Jeste li ovako zamišljali ono što ste zapisali? ',
      'math_query_answer': 'Rješenje je ',
      'goodbye': 'Doviđenja.'
    }
  }

  language_select_file = createSoundFile('language_select', 'Hello, please select your language by entering the words english or croatian then pressing the "Enter" key.', 'en')
  print('Hello, please select your language by entering the words english or croatian then pressing the "Enter" key.')
  playsound(language_select_file)

  language_select = input()

  language = getLanguage(language_select) #'english' or 'hrvatski'

  #print(language)

  #preloading files
  greeting_file = createSoundFile('greeting', selected_language[language]['greeting'], language[:2])
  manual_prompt_file = createSoundFile('manual_prompt', selected_language[language]['manual_prompt'], language[:2])
  math_query_file = createSoundFile('math_query', selected_language[language]['math_query'], language[:2])
  goodbye_file = createSoundFile('goodbye', selected_language[language]['goodbye'], language[:2])

  print(selected_language[language]['greeting'])
  playsound(greeting_file)

  print(selected_language[language]['manual_prompt'])
  playsound(manual_prompt_file)

  prompt = checkInput(input())

  if prompt is True:

    manual_file = createSoundFile('manual', selected_language[language]['manual'], language[:2])
    print(selected_language[language]['manual'])
    playsound(manual_file)

  print(selected_language[language]['math_query'])
  playsound(math_query_file)

  problem = input()

  if problem == '':

    math_query_empty_file = createSoundFile('math_query_empty', selected_language[language]['math_query_empty'], language[:2])

    while problem == '':

      playsound(math_query_empty_file)
      problem = input()

  print(selected_language[language]['math_query_prompt'] + problem)
  math_query_prompt_file = createSoundFile('math_query_prompt', selected_language[language]['math_query_prompt'] + problem, language[:2])
  playsound(math_query_prompt_file)

  prompt2 = checkInput(input())

  if prompt2 is True:
    
    answer = doMaths(problem)

    print(selected_language[language]['math_query_answer'] + answer)
    math_query_answer_file = createSoundFile('math_query_answer', selected_language[language]['math_query_answer'] + answer, language[:2])
    playsound(math_query_answer_file)

    print(selected_language[language]['goodbye'])
    playsound(goodbye_file)

  else:

    print(selected_language[language]['goodbye'])
    playsound(goodbye_file)