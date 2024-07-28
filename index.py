import random

anime_dict = {
    'Naruto': ('A story about a young ninja striving to become the strongest in his village.', 7.81),
    'Attack on Titan': ('Humanity fights for survival against giant humanoids.', 8.83),
    'Death Note': ('A student finds a notebook that kills anyone whose name is written in it.', 8.63),
    'One Piece': ('Adventures of pirates searching for the world’s greatest treasure.', 8.69),
    'My Hero Academia': ('A boy without superpowers strives to become the greatest hero.', 7.88),
    'Fullmetal Alchemist: Brotherhood': ('Two brothers search for a way to restore their bodies after a failed experiment.', 9.10),
    'Sword Art Online': ('Players are trapped in a virtual reality game and must clear it to survive.', 7.27),
    'Demon Slayer': ('A young man becomes a demon slayer to save his sister.', 8.67),
    'Tokyo Ghoul': ('A young man becomes a half-ghoul and tries to survive in his new world.', 7.87),
    'One Punch Man': ('A hero who defeats all enemies with one punch seeks a worthy opponent.', 8.38),
    'Steins;Gate': ('A group of friends accidentally discover a method of time travel.', 9.11),
    'Hunter x Hunter': ('A young boy embarks on a journey to find his father and become a Hunter.', 9.00),
    'Fairy Tail': ('Members of a magical guild go on various adventures together.', 7.67),
    'Sword Art Online: Alicization': ('Continuation of the virtual reality adventures in Sword Art Online.', 7.53),
    'Code Geass': ('A young man gains the power of absolute obedience and leads a rebellion.', 8.71),
    'Black Clover': ('Two orphans strive to become the Wizard King in a world of magic.', 7.99),
    'Re:Zero - Starting Life in Another World': ('A boy is transported to another world where he has the ability to reset time.', 8.30),
    'The Seven Deadly Sins': ('A group of knights must band together to save their kingdom.', 7.70),
    'Dragon Ball Z': ('Warriors with extraordinary powers protect Earth from powerful foes.', 8.15),
    'Neon Genesis Evangelion': ('Teenagers pilot giant robots to protect Earth from mysterious beings.', 8.32),
    'Cowboy Bebop': ('Bounty hunters travel through space in pursuit of criminals.', 8.76),
    'Your Lie in April': ('A piano prodigy rediscovers his love for music through a spirited violinist.', 8.79),
    'Clannad': ('A delinquent student finds new meaning in life through new friendships.', 8.09),
    'Toradora!': ('A misunderstood girl and a boy with a fierce look form an unexpected friendship.', 8.15),
    'Spirited Away': ('A young girl becomes trapped in a mysterious world and must find her way out.', 8.84),
    'My Neighbor Totoro': ('Two girls discover magical creatures in the forest near their new home.', 8.24),
    'Princess Mononoke': ('A young warrior gets involved in a struggle between nature and industrialization.', 8.70),
    'Howl’s Moving Castle': ('A young woman cursed with an old body meets a wizard and gets involved in his world.', 8.64),
    'Akira': ('A biker gang member in post-apocalyptic Tokyo gains powerful psychic abilities.', 8.17),
    'Ghost in the Shell': ('A cyborg policewoman hunts a mysterious hacker.', 8.29),
    'Psycho-Pass': ('In a dystopian future, police officers use a system that predicts crimes.', 8.39),
    'Paranoia Agent': ('A series of mysterious attacks by a figure on rollerblades.', 7.62),
    'Samurai Champloo': ('A girl seeks the samurai who smells of sunflowers, accompanied by two swordsmen.', 8.50),
    'Mob Psycho 100': ('A boy with psychic powers tries to live a normal life.', 8.51),
    'Kill la Kill': ('A girl searches for her father’s killer while attending a school where students wear powerful uniforms.', 7.86),
    'Yu Yu Hakusho': ('A teenager becomes a spirit detective after dying and returning to life.', 8.49),
    'Rurouni Kenshin': ('A wandering swordsman protects those in need while seeking redemption for his past.', 8.31),
    'Berserk': ('A lone mercenary fights his way through a dark, medieval world.', 8.38),
    'Trigun': ('A gunman with a high bounty travels through a desert planet, causing chaos.', 8.23),
    'Fate/Zero': ('Seven mages summon heroic spirits to fight in a battle royale for the Holy Grail.', 8.34),
    'Hellsing': ('A vampire works for a secret organization to protect England from supernatural threats.', 7.54),
    'Death Parade': ('People are judged in the afterlife through various games.', 8.21),
    'Made in Abyss': ('A girl and a robot descend into a vast, dangerous chasm to find her mother.', 8.68),
    'The Promised Neverland': ('Children at an orphanage discover the dark secret behind their existence.', 8.46),
    'Violet Evergarden': ('A former soldier becomes a letter writer to understand human emotions.', 8.69),
    'Your Name': ('Two teenagers swap bodies and learn to understand each other’s lives.', 8.80),
    'Anohana: The Flower We Saw That Day': ('A group of friends reunites to help the spirit of a deceased friend move on.', 8.40),
    'March Comes in Like a Lion': ('A young professional shogi player struggles with personal issues.', 8.47),
    'Haikyuu!!': ('A high school volleyball team strives to become the best in Japan.', 8.77),
    'K-On!': ('A group of high school girls form a band and experience the joys of music and friendship.', 7.84),
    'Great Teacher Onizuka': ('A former gangster becomes a high school teacher to inspire students.', 8.70),
    'No Game No Life': ('Siblings are transported to a world where games decide everything.', 8.14),
    'Erased': ('A man with the ability to travel back in time tries to prevent a tragedy.', 8.34),
    'Gintama': ('A samurai and his friends take on odd jobs in an alternate-history Japan.', 8.97),
    'Mushishi': ('A traveler investigates supernatural creatures called Mushi.', 8.68)
}

def random_():
    random_anime=random.choice(list(anime_dict))
    return random_anime

def get_anime(anime):
    anime_desc=anime_dict[anime][0]
    return anime + ", " + anime_desc
    
def get_rating(anime):
    anime_rating=anime_dict[anime][1]
    return anime_rating
    
def compare(anime1, anime2):
    first=get_rating(anime1)
    second=get_rating(anime2)
    if first>second:
        return True
    elif first<second:
        return False
      
score = 0

while True:
    anime1 = random_()
    anime2 = anime1
    while anime2 == anime1:
        anime2 = random_()
    
    print("Your score is " + str(score))
    print("Compare A: " + get_anime(anime1))
    print("Compare B: " + get_anime(anime2))
    
    ask=input("Which anime has higher SHIKIMORI rating? Type 'A' or 'B': ").upper()
    
    if ask=="A":
        result = compare(anime1, anime2)
    elif ask=="B":
        result = compare(anime2, anime1)
    else: 
        print("Incorrect input. Please try again")
        continue
        
    if result == False:
        print(f"You are wrong:\n {anime1} rating: {get_rating(anime1)}\n {anime2} rating: {get_rating(anime2)}")
        print(f"Your final score: {score}")
        break
    else:
        print("You are absolutely right!!!")
        score += 1



