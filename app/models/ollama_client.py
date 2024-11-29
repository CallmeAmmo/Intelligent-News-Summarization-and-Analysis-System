from ollama import AsyncClient
import asyncio

class ollama_client():

    def __init__(self, model, url):
        self.model = model
        self.url = url
    
    async def summarize_text(self, text):

        message = [
                    {'role':'system', 'content': 'You are a helpful assistant and you task is to summarize the text in 50 words.'},
                    {'role':'user', 'content': text}
        ]

        client = AsyncClient(host = self.url)
        response = await client.chat(model=self.model, messages=message)
        return response['message']['content']


    async def summarize_text_stream(self, text):

        message = [
                    {'role':'system', 'content': 'You are a helpful assistant and you task is to summarize the text in 50 words.'},
                    {'role':'user', 'content': text}
        ]

        client = AsyncClient(host = self.url)
        async for part in await client.chat(model=self.model, messages=message, stream=True):
            yield part['message']['content']


# if __name__ == "__main__":
#     r = '''
#         Advertisement\n\nKalshi and Polymarket made waves this election as billions of dollars were bet on the outcome.\n\nKalshi launched election betting for US citizens after winning court approval in early October.\n\nNow that the election is over, here\'s what people are betting on in prediction markets.\n\nBillions of dollars were bet on the presidential election outcome via prediction market platforms like Kalshi and Polymarket.\n\nIt was a new phenomenon in election cycles, with Kalshi receiving court approval in early October to launch election-based betting contracts for US citizens.\n\nAdvertisement\n\nBetting sites garnered particular attention for diverging from the polls, though the prediction markets turned out to be largely correct. Trump was favored to win the election throughout the month of October on Kalshi and Polymarket, while most polls had the candidates locked in a dead heat.\n\nWith the election over, money is now flowing into other bets on the platform, from everything from Rotten Tomato movie scores to the winner of the upcoming Mike Tyson vs. Jake Paul fight.\n\nHere are some of the most popular bets on Kalshi and Polymarket now that the election is over.\n\nAdvertisement\n\nSuper Bowl Champion 2025\n\nThe Chargers and Chiefs last faced off in January 2024. Ryan Kang/Getty Images\n\nCurrent odds: Chiefs (18¢), Lions (16¢), Ravens (13¢), Bills (9¢), 49ers (8¢), Eagles (7¢), Packers (3¢), Commanders (3¢), Steelers (3¢)\n\nBetting volume: $751.0 million\n\nWill Biden finish his term?\n\nPresident Joe Biden AP Photo/Susan Walsh\n\nCurrent odds: Yes (93¢), No (8¢)\n\nBetting volume: $33.3 million\n\nJake Paul vs. Mike Tyson: Who will win?\n\nJake Paul during a 2023 fight. Sam Hodde/Getty Images\n\nCurrent odds: Jake Paul (64¢), Mike Tyson (27¢), Draw (11¢)\n\nBetting volume: $5.0 million\n\nAdvertisement\n\nWill Bitcoin hit $100k in 2024?\n\nBitcoin is above $90,000 on Wednesday. SOPA Images / Getty\n\nCurrent odds: Yes (73¢), No (30¢)\n\nBetting volume: $3.5 million\n\nNext Senate Majority Leader?\n\nFrom left: Sens. John Thune, Rick Scott, and John Cornyn are all officially running to succeed Mitch McConnell. Alex Wong, Andrew Harnik, and Kevin Dietsch/Getty Images\n\nCurrent odds: John Thune (64¢), Rick Scott (26¢), John Cornyn (11¢)\n\nBetting volume: $2.0 million\n\nNext James Bond actor?\n\nMGM\n\nCurrent odds: Aaron Taylor-Johnson (9¢), Henry Cavill (5¢), Damson Idris (3¢), Rege-Jean Page (1¢), Cosmo Jarvis (1¢), Tom Hardy (1¢), Other (80¢)\n\nAdvertisement\n\nBetting volume: $448,398\n\nTaylor Swift engaged in 2024?\n\nTaylor Swift and Scott Swift at a Chief\'s game in December 2023. Kathryn Riley/Getty Images\n\nCurrent odds: Yes (12¢), No (90¢)\n\nBetting volume: $397,339\n\nWho will be the Billboard #1 pop star of the century?\n\nKevin Mazur/WireImage for Parkwood\n\nCurrent odds: Taylor Swift (78¢), Beyonce (21¢), Rihanna (2¢), Other (1¢)\n\nBetting volume: $387,787\n\nAdvertisement\n\n"Wicked" Rotten Tomatoes Score?\n\nAriana Grande at a photocall for "Wicked" in November 2024. Don Arnold/WireImage/Getty Images\n\nCurrent odds: Above 95 (19¢), Above 90 (48¢), Above 85 (75¢), Above 80 (78¢), Above 75 (80¢)\n\nBetting volume: $299,765\n\nWill Trump say "mog" in 2024?\n\nPresident-elect Donald Trump Bill Pugliano/Getty Images\n\nCurrent odds: Yes (9¢), No (93¢)\n\nBetting Volume: $162,099
#         '''


#     # from app.models.ollama_client import ollama_client
#     import asyncio
#     a = ollama_client('llama3.2', 'http://localhost:11434')

#     async def main():
#         async for text in a.summarize_text_stream(r):
#             print(text, end='', flush=True)
            


#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())  # This runs until the 'main' function is finished

