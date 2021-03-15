import http.client
import json
import urllib

class WarzoneStats:
    def __init__(self, gametag, platform):
        self.gametag = gametag
        self.platform = platform

    def __search_profile(self):
        conn = http.client.HTTPSConnection("call-of-duty-modern-warfare.p.rapidapi.com")
        user = self.__gametag_transform(self.gametag) if self.platform == 'Battle.net'  else  self.gametag
        platforms = { 'PlayStation': 'psn', 'Steam': 'steam', 'Xbox Live':'xbl', 'Battle.net':'battle'}
        headers = {
            'x-rapidapi-host': "call-of-duty-modern-warfare.p.rapidapi.com",
            'x-rapidapi-key': "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" # Your api key
            }
        conn.request("GET", f"/warzone/{user}/{platforms.get(self.platform)}", headers=headers)
        res = conn.getresponse()
        data = res.read()
        all_data = json.loads(data.decode("utf-8"))

        return all_data
    
    def classify_stats(self):
        data = self.__search_profile()
        error = data.get('error')
        if error == True:
            message = data.get('message')
            battle = None
            battle_wins = None
            plunder = None
            plunder_wins = None
            all_br = None
            all_wins = None
        else:
            message = None
            battle_royale = data.get('br')
            br_kdr = battle_royale.get('kdRatio')
            br_kills = str(battle_royale.get('kills'))
            br_deaths = str(battle_royale.get('deaths'))
            br_downs = str(battle_royale.get('downs'))
            br_revives = str(battle_royale.get('revives'))
            br_wins = str(battle_royale.get('wins'))
            
            battle = f"Kill/Death Ratio: {br_kdr:.2f}"+"\nKills: "+br_kills+"\nDeaths: "+br_deaths+"\nDowns: "+br_downs+"\nRevives: " + br_revives
            battle_wins = "WINS:\n" + br_wins

            battle_dmz = data.get('br_dmz')
            brDmz_kdr = battle_dmz.get('kdRatio')
            brDmz_kills = str(battle_dmz.get('kills'))
            brDmz_deaths = str(battle_dmz.get('deaths'))
            brDmz_downs = str(battle_dmz.get('downs'))
            brDmz_revives = str(battle_dmz.get('revives'))
            brDmz_wins = str(battle_dmz.get('wins'))

            plunder = f"Kill/Death Ratio: {brDmz_kdr:.2f}"+"\nKills: "+brDmz_kills+"\nDeaths: "+brDmz_deaths+"\nDowns: "+brDmz_downs+"\nRevives: " + brDmz_revives
            plunder_wins = "WINS:\n" + brDmz_wins

            battle_all = data.get('br_all')
            all_kdr = battle_all.get('kdRatio')
            all_kills = str(battle_all.get('kills'))
            all_deaths = str(battle_all.get('deaths'))
            all_downs = str(battle_all.get('downs'))
            all_revives = str(battle_all.get('revives'))
            all_wins = str(battle_all.get('wins'))
            
            all_br = f"Kill/Death Ratio: {all_kdr:.2f}"+"\nKills: "+all_kills+"\nDeaths: "+all_deaths+"\nDowns: "+all_downs+"\nRevives: " + all_revives
            all_wins = "WINS:\n" + all_wins

        return message, battle, battle_wins, plunder, plunder_wins, all_br, all_wins

    def __gametag_transform(self,gametag):
        new_gametag = urllib.parse.quote_plus(gametag)
        return new_gametag


