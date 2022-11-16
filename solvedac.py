from requests import get

def tiermaker(tier: int):
    tiers = ["Unranked", "Bronze V", "Bronze IV", "Bronze III", "Bronze II", "Bronze I", "Silver V", "Silver IV", "Silver III", "Silver II", "Silver I", "Gold V", "Gold IV", "Gold III", "Gold II", "Gold I", "Platinum V", "Platinum IV", "Platinum III", "Platinum II", "Platinum I", "Diamond V", 
             "Diamond IV", "Diamond III", "Diamond II", "Diamond I", "Ruby V", "Ruby IV", "Ruby III", "Ruby II", "Ruby I", "Master"]
    return tiers[tier]

class SolvedACUser:
    def __init__(self, name):
        self.name = name
        apire = get("https://solved.ac/api/v3/user/show", params={"handle": name}, headers={"Content-Type": "application/json"}).json()
        self.bio = apire["bio"]
        self.organizations = apire["organizations"]
        self.badge = apire["badge"]
        self.background = apire["background"]
        self.profileimage = apire["profileImageUrl"]
        self.solved = apire["solvedCount"]
        self.cla = apire["class"]
        self.classDecoration = apire["classDecoration"]
        self.tier = tiermaker(apire["tier"])
        self.rating = apire["rating"]
        self.ratingByProblemsSum = apire["ratingByProblemsSum"]
        self.ratingByClass = apire["ratingByClass"]
        self.ratingByVoteCount = apire["ratingByVoteCount"]
        self.exp = apire["exp"]
        self.rivalCount = apire["rivalCount"]
        self.reverseRivalCount = apire["reverseRivalCount"]
        self.maxStreak = apire["maxStreak"]
        self.proUntil = apire["proUntil"]
        self.rank = apire["rank"]

