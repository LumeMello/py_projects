import pandas as pd

file_path = "Banco De Dados do Fliperama.xlsx"

df = pd.read_excel(file_path, sheet_name="Planilha1")

def infer_genre(game_name):
    name = str(game_name).lower()

    # Racing
    if any(word in name for word in ["rally", "racer", "racing", "kart", "drift", "gran turismo", "need for speed", "cruis'n", "outrun", "daytona"]):
        return "Racing"
    # Fighting
    elif any(word in name for word in ["street fighter", "mortal kombat", "tekken", "king of fighters", "samurai shodown", "virtua fighter", "fighter"]):
        return "Fighting"
    # Beat 'em up
    elif any(word in name for word in ["double dragon", "final fight", "streets of rage", "tmnt", "turtles", "x-men arcade", "simpsons arcade"]):
        return "Beat 'em up"
    # Sports
    elif any(word in name for word in ["soccer", "football", "basketball", "nba", "fifa", "nhl", "tennis", "golf", "boxing"]):
        return "Sports"
    # Maze
    elif any(word in name for word in ["pac-man", "pacman", "maze", "labyrinth"]):
        return "Maze"
    # Shooter
    elif any(word in name for word in ["invaders", "asteroids", "defender", "galaga", "phoenix", "1942", "1943", "raiden"]):
        return "Shooter"
    # Shoot 'em up
    elif any(word in name for word in ["shoot", "blaster", "shooter", "gun", "space harrier", "gradius", "r-type", "ikari warriors"]):
        return "Shoot'em up"
    # Puzzle
    elif any(word in name for word in ["puzzle", "tetris", "columns", "bust-a-move", "dr mario", "lemmings"]):
        return "Puzzle"
    # Aventura e Exploração
    elif any(word in name for word in ["adventure", "quest", "myst", "explorer", "indiana jones", "pitfall"]):
        return "Aventura e Exploração"
    # Plataformer
    elif any(word in name for word in ["mario", "donkey kong", "sonic", "plumber", "rayman", "earthworm jim"]):
        return "Plataformer"
    # RPG
    elif any(word in name for word in ["rpg", "fantasy", "dragon quest", "final fantasy", "zelda", "chronotrigger", "breath of fire"]):
        return "RPG"
    # Horror
    elif any(word in name for word in ["resident evil", "silent hill", "house of the dead", "castlevania", "alone in the dark"]):
        return "Horror"
    # Strategy
    elif any(word in name for word in ["strategy", "warcraft", "command", "age of empires", "civilization", "starcraft"]):
        return "Strategy"
    # Run and Gun
    elif any(word in name for word in ["metal slug", "contra", "gunstar heroes", "sunset riders"]):
        return "Run and Gun"
    # Rhythm / Music
    elif any(word in name for word in ["dance dance", "guitar hero", "parappa", "osu", "beatmania"]):
        return "Music / Rhythm"
    # Farm
    elif any(word in name for word in ["harvest", "stardew"]):
        return "Farm"

    return ""

df["Generos"] = df.apply(
    lambda row: infer_genre(row["Jogo"]) if pd.isna(row["Generos"]) else row["Generos"],
    axis=1
)

output_path = "Banco_De_Dados_Fliperama_Preenchido.xlsx"
df.to_excel(output_path, index=False)

print(f"Arquivo salvo em: {output_path}")
