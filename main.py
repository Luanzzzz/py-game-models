import json
from db.models import Race, Skill, Player, Guild


def main():
    with open('players.json', 'r') as file:
        data = json.load(file)

    for player_data in data:
        # 1. Lidar com a Raça (Race)
        # O get_or_create retorna (objeto, created_boolean). Pegamos o índice [0].
        race_data = player_data['race']
        race_obj, _ = Race.objects.get_or_create(
            name=race_data['name'],
            defaults={'description': race_data.get('description', '')}
        )

        # 2. Lidar com as Skills (dentro da Raça)
        # Iteramos sobre a lista de skills dentro dos dados da raça
        for skill_data in race_data.get('skills', []):
            Skill.objects.get_or_create(
                name=skill_data['name'],
                defaults={
                    'bonus': skill_data['bonus'],
                    'race': race_obj  # Ligamos a skill à raça criada acima
                }
            )

        # 3. Lidar com a Guilda (Guild)
        guild_data = player_data['guild']
        guild_obj = None

        # Verificação de segurança caso o jogador não tenha guilda no JSON
        if guild_data:
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_data['name'],
                defaults={'description': guild_data.get('description')}
            )

        # 4. Criar o Player
        # Aqui usamos create() ou get_or_create() para o player.
        # Como o nickname é unique, get_or_create é mais seguro se rodar o script 2 vezes.
        Player.objects.get_or_create(
            nickname=player_data['nickname'],
            defaults={
                'email': player_data['email'],
                'bio': player_data['bio'],
                'race': race_obj,  # Objeto Race obtido no passo 1
                'guild': guild_obj  # Objeto Guild obtido no passo 3
            }
        )


if __name__ == "__main__":
    main()