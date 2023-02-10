import requests
params={
    "amount":10,
    "category":18,
    "type":"boolean"
}

#api call for getting data from the endpoint and here we send some parameter to the website.
response=requests.get(url='https://opentdb.com/api.php',params=params)
response.raise_for_status()
question_data=response.json()["results"]
# response=requests.get(url='https://opentdb.com/api.php',params=params)
# response.raise_for_status()
# r={"response_code":0,"results":[{"category":"Vehicles","type":"boolean","difficulty":"medium","question":"The Chevrolet Corvette has always been made exclusively with V8 engines only.","correct_answer":"False","incorrect_answers":["True"]},{"category":"Entertainment: Film","type":"boolean","difficulty":"easy","question":"In the original script of &quot;The Matrix&quot;, the machines used humans as additional computing power instead of batteries.","correct_answer":"True","incorrect_answers":["False"]},{"category":"Entertainment: Cartoon & Animations","type":"boolean","difficulty":"easy","question":"Bill Cipher in the show &quot;Gravity Falls&quot; is the good guy.","correct_answer":"False","incorrect_answers":["True"]},{"category":"General Knowledge","type":"boolean","difficulty":"easy","question":"The color orange is named after the fruit.","correct_answer":"True","incorrect_answers":["False"]},{"category":"Entertainment: Television","type":"boolean","difficulty":"medium","question":"The television show Doctor Who first aired in 1963.","correct_answer":"True","incorrect_answers":["False"]},{"category":"History","type":"boolean","difficulty":"hard","question":"The USS Missouri (BB-63) last served in the Korean War.","correct_answer":"False","incorrect_answers":["True"]},{"category":"Entertainment: Japanese Anime & Manga","type":"boolean","difficulty":"medium","question":"In &quot;JoJo&#039;s Bizarre Adventure&quot;, Father Enrico Pucchi uses a total of 3 stands in Part 6: Stone Ocean.","correct_answer":"True","incorrect_answers":["False"]},{"category":"Science: Mathematics","type":"boolean","difficulty":"easy","question":"An equilateral triangle always has every angle measuring 60&deg;.","correct_answer":"True","incorrect_answers":["False"]},{"category":"History","type":"boolean","difficulty":"medium","question":"Sir Issac Newton served as a Member of Parliament, but the only recorded time he spoke was to complain about a draft in the chambers.","correct_answer":"True","incorrect_answers":["False"]},{"category":"Animals","type":"boolean","difficulty":"easy","question":"The freshwater amphibian, the Axolotl, can regrow it&#039;s limbs.","correct_answer":"True","incorrect_answers":["False"]}]}
# question_data=r["results"]