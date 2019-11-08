import csv
import random

names = ['Cas Haley', 'Caspa Codina', 'Clarian', 'Catfish Submarine',
       'Naughty Altar Boy', 'Jaymo & Andy George, Sidney Charles',
       'CeCe Winans', 'Banda 3 Rios', 'Nick Jonas', 'Monoxide',
       'Lmfao Karaoke Band', 'Obey City', 'Sandy Rivera feat. Haze',
       'Ella Henderson', 'Chase', 'RAC', 'BeyoncÌ© featuring Voltio',
       'Tony Bennett and Lady Gaga', 'Once Jamison', 'Omi',
       'OMI feat. Kid Ink', 'OMI feat. Nicky Jam', 'Andra Day',
       'TV On The Radio', 'Pink B', 'Jack Houston', 'Rewind',
       'Sopor Aeternus, The Ensemble Of Shadows', 'Sing Top 10',
       'Worldwide Groove Corporation', 'Alyxx Dione feat. Jason Derulo',
       'Bob Weinberg', "Art Bernstein & Chuck D'Aloia (Abcd)",
       'Benny Benassi feat. Gary Go', 'Benny Benassi', 'Dj Happee',
       'Walter Mayers', 'Steven R. Smith', 'City High',
       'Alesso and Dirty South', 'David Guetta & Glowinthedark', 'Alesso',
       'Good Guy Mikesh & Filburt', 'Doorly and Shadow Child',
       'Nathaniel Rateliff', 'Flo Rida', 'Varios Artistas',
       'Inna Zhelannaya',
       'Excision, Dion Timmer, The Frim, Downlink, Space Laces, Pegboard Nerds',
       'Wynonna', 'Third Party feat. Daniel Gidlund', 'Style of Eye',
       'Paris Blohm and Tritonal', 'Headhunterz feat. Tatu', 'Yuna',
       'Sunnery James & Ryan Marciano featuring KiFi', "Cam'Ron",
       'Sandy Rivera featuring LT Brown', 'Ultimate Party Jams',
       'HOT 100', 'Years & Years', 'Eric Clapton', 'Quiet Riot',
       'Queensryche', 'Demi Lovato', 'The Devlins', 'Night Riots',
       'Anthony Hamilton featuring David Banner',
       'Aaron Copland, London Symphony Orchestra, William Warfield',
       'Chase Rice', 'Shake It for Me', 'Roy Herzer', 'Monkey Safari',
       'Luke Bryan',
       'David Miller, Lawrence Bartlett, Paul Hooper, Sven Libaek',
       'Excision & Downlink', 'Buddy Miller', 'Melanie Martinez',
       'Kristinia DeBarge', 'Katy B', 'Olympique',
       'ChocQuibTown feat. Nicky Jam', 'Pollie Pop', 'Elle & Him',
       'Nicky Jam', 'I Am Oak', 'Eminem', 'Antony And The Johnsons',
       'Kyla La Grange & Kygo', 'Jason Derulo', 'Cypress Hill & Rusko',
       'Style Of Eye, Magnus the Magnus', 'Daya',
       'DH Lawrence Read By David Shaw-Parker', 'Caspa Houzer',
       'DJ Snake MacHine', 'Breach aka Ben Westbeech',
       'DNA British Pop Band', 'British Pop Band', 'Walk the Moon',
       'Benny Benassi feat. John Legend', 'Whitney Houston',
       'Icicle Work', 'A Tributer',
       'DaVinChe featuring Wretch 32 and Cleo Sol', 'Didrik Thulin',
       'Howard Hersh, James Winn & Patricia Shands', 'David Guetta',
       'Perturbator', 'Dianne Dugaw', 'Wayne Devlin', 'Don Omar',
       'The Summer Hits Band', 'Hardwell feat. Matthew Koma',
       'Breaking Benjamin', 'BT and Gregory Tripi', 'Carnage',
       'The Theme Tune Kids', 'Epic Rap Battles of History',
       'Star Wars Ringtones', 'Dave Devlin', 'Ookla the Mok',
       'Mark Lawrence', 'Kid Cudi', 'Daya Lorin', 'Spencer Day',
       'Kelly Rowland featuring Travis McCoy of Gym Class Heroes',
       'Dominique Vellard, HervÌ© Lamy, Pierre Hamon, Philippe Balloy, Willem De Waal, Jaques Bona, Ensemble Gilles Binchois, Dominique Vellard, Andreas Scholl, Gerd TÌ_rk, Emmanuel Bonnardot, Jean-Paul Racodon',
       'Third Party & Nick Sheldon', 'Dead Sara', 'A Breach of Silence',
       'Tribute To Olly Murs', 'Willie Nelson and Sister Bobbie',
       'The Submarines', 'Lil Wayne, Dj Drama', 'Lil Wayne',
       'George Fenton & Berlin Philharmonic Orchestra', 'Joe Scruggs',
       'Wideboys, Ruff Driverz', 'Blake Stone', 'String Tribute Players',
       'Shemekia Copeland', 'Colin Devlin', 'Le Caribou Volant',
       'Al Bizzare feat. Alateya', "Destiny's Child",
       'Various Artists, Excision, Space Laces, Downlink, Bassnectar, Far Too Loud, Ajapai',
       'Various Artists, Excision, Downlink, Space Laces, Bassnectar, Far Too Loud, Ajapai',
       'Excision & Space Laces', 'Excision and Ajapai, Excision, Ajapai',
       'Frou Frou', 'DJ Covers', 'The Tony Rice Unit', 'Jessie Ware',
       'Sonik - Omi', 'King Creosote & Jon Hopkins', 'Radio Remix',
       'Karaoke Hitts', 'Karaoke Pro', 'Test Icicles', 'DJ Cam Quartet',
       'Breach', 'Ali Love', "I'm Chillin On a Dirt Road",
       'Jason Aldean feat. Ludacris', 'Granger Smith', 'Old Dominion',
       'Zombie Platypus Conspiracy', 'D.R.I.', 'Starkillers',
       'Loefah & Coki', 'various artisits', 'Launch Party',
       'Lifelike & Kris Menace', 'Toni Braxton', 'Kyau & Albert',
       'Stuart McCallum (of the Cinematic Orchestra)', 'Passenger',
       'Wyclef Jean feat. Avicii', 'Voltio',
       'Willie Nelson & Merle Haggard', 'Glee Cast', 'The Game',
       'Dog, Paper, Submarine', 'Snoop Doggy Dogg', 'Ringtone Spy',
       'Wretch 32 feat. Jacob Banks', 'Granite Karaoke',
       'Dolly Parton, Kenny Rogers', 'Karaoke Boulevard',
       'Pinchers, Bounty Killer', 'The True Star',
       'Joey Negro Pres?Akabu', 'Montana Express & Thomas Gold',
       'The Beastie Boys', 'Zoom Karaoke', 'Sam Skilz, A. Lee', 'Rihanna',
       'Systematic vs. Thomas Gold',
       'Jake Bruene & Clara Chung feat. Kurt Schneider & Kevin Olusola',
       'Swedish House Mafia', 'M.A.N.D.Y. vs. Booka Shade',
       'Joey Negro presents Doug Willis',
       'Mark Knight, D.Ramirez, Underworld',
       'Our Last Night feat. Matty Mullins', 'One Direction', 'Vance Joy',
       'OneRepublic', 'Mr. Probz', 'Therese',
       'The Crystal Method featuring Matisyahu', 'Billy Cobham',
       'Good Guy Mikesh', 'Late Night Alumni',
       'Duel and Gavyn Wright and London Session Orchestra',
       'Various Artists & The Naughty Boys From Nashville',
       'Lee Wiley & Ellis Larkins', 'Steven Lee Adams', 'Inna Poroshina',
       'Andrea Bocelli and Ariana Grande',
       'The Squatters feat. Kissy Sell Out',
       'Naomi, Christina (Wynonna) Judd, Pete Charles',
       'JayW.GuitarSlinger']
mF = ['male' , 'female', 'mixed']
gender = []
country = ['United States','Korea','South America','Spain','Britian','France']
origin = []
# arrLen = len(names)
for x in names:
    gender.append(random.choice(mF))
for x in range(len(names)):
    if x % 2 == 0 or x % 3 == 0 or x % 5 == 0 or x % 7 == 0: 
        origin.append(country[0])
    else:
        origin.append(random.choice(country))
RESULTS = [
    names,
    gender,
    origin
]
out = [list(x) for x in zip(*RESULTS)]
with open("output.csv",'w') as resultFile:
    wr = csv.writer(resultFile, dialect='excel')
    wr.writerows(out)