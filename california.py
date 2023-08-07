import openai
import random

openai.api_key = "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"

lyrics = """
Greetings loved ones
Let's take a journey
I know a place
Where the grass is really greener
Warm, wet n' wild
There must be something in the water
Sippin' gin and juice
Laying underneath the palm trees
(Undone)
The boys
Break their necks
Try'na to creep a little sneak peek
(At us)
You could travel the world
But nothing comes close
To the golden coast
Once you party with us
You'll be falling in love
Ooh oh ooh oh oh ooh
California girls
We're unforgettable
Daisy dukes
Bikinis on top
Sun-kissed skin
So hot
We'll melt your popsicle
Ooh oh ooh
Ooh oh ooh
California girls
We're undeniable
Fine, fresh, fierce
We got it on lock
West coast represent
Now put your hands up
Ooh oh ooh
Ooh oh ooh
Sex on the beach
We don't mind sand in our stilettos
We freak
In my jeep
Snoop doggy-dog on the stereo oh oh
You could travel the world
But nothing comes close
To the golden coast
Once you party with us
You'll be falling in love
Ooh oh ooh ooh oh ooh
California girls
We're unforgettable
Daisy dukes
Bikinis on top
Sun-kissed skin
So hot
We'll melt your popsicle
Ooh oh ooh
Ooh oh ooh
California girls
We're undeniable
Fine, fresh, fierce
We got it on lock
West coast represent
Now put your hands up
Ooh oh ooh
Ooh oh ooh
Toned, tan
Fit and ready
Turn it up 'cause its gettin' heavy
Wild, wild west coast
These are the girls I love the most
I mean the ones
I mean like she's the one
Kiss her, touch her
Squeeze her buns
The girl's a freak
She drive a jeep
And live on the beach
I'm okay
I won't play
I love the bay
Just like I love L.A.
Venice Beach
And Palm Springs
Summertime is everything
Home boys
Bangin' out
All that ass
Hanging out
Bikinis, zucchinis, martinis
No weenies
Just a king
And a queenie
Katy my lady
(Yeah)
And looky here baby
(Uh huh)
I'm all up on ya
'Cause you representing California (oh yeah)
California girls
We're unforgettable
Daisy dukes
Bikinis on top
Sun-kissed skin
So hot
We'll melt your popsicle
Ooh oh ooh
Ooh oh ooh
California girls
We're undeniable
Fine, fresh, fierce
We got it on lock
West coast represent (west coast, west coast)
Now put your hands up
Ooh oh ooh
Ooh oh ooh
California girls man
(California)
(California girls)
"""

lyrics_array = lyrics.strip().split('\n')



def run_lyric_matcher(score, runs):
    line_number = random.randint(0, len(lyrics_array) - 1)
    lyric_question = lyrics_array[line_number]
    song_name = "California Gurls"
    artist = "Katy Perry, Snoop"
    question = 'What is the next lyric in the sequence for {song}, the hit song from {artist}? The current lyric is "{lyric}".'.format(song=song_name, artist=artist, lyric=lyric_question)

    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": question}])
    answer = chat_completion.choices[0].message.content

    print(question)
    print(answer)
    if answer in lyrics:
        score += 1
    runs += 1
    return [score, runs]

def main():
    score = 0
    runs = 0

    for run_num in range(100):
        [score, runs] = run_lyric_matcher(score, runs)

    

    print("{score} / {runs}, {percentage}".format(score=score, runs=runs, percentage=score / runs * 100))

main()

# with 40 runs, the success rate was 17.5%
# with 100 runes, the success rate was 6%