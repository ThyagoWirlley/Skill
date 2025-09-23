import streamlit as st

skill_map = {
    "Mind": 0, "Body": 1, "Soul": 2, "Body Control": 3, "Body Stamina": 4,
    "Body Strength": 5, "Mind Logic": 6, "Mind Speed": 7, "Soul Depth": 8,
    "Soul Strength": 9, "Swords": 10, "Axes": 11, "Knives": 12, "Mauls": 13,
    "Clubs": 14, "Hammers": 15, "Archery": 16, "Polearms": 17, "Tailoring": 18,
    "Cooking": 19, "Smithing": 20, "Weapon Smithing": 21, "Armour smithing": 22,
    "Miscellaneous Items": 23, "Shields": 24, "Alchemy": 25, "Nature": 26, "Toys": 27,
    "Fighting": 28, "Healing": 29, "Religion": 30, "Thievery": 31,
    "War Machines": 32, "Farming": 33, "Papyrusmaking": 34, "Thatching": 35,
    "Gardening": 36, "Meditating": 37, "Forestry": 38, "Rake": 39, "Scythe": 40,
    "Sickle": 41, "Small Axe": 42, "Mining": 43, "Digging": 44, "Pickaxe": 45,
    "Shovel": 46, "Pottery": 47, "Ropemaking": 48, "Woodcutting": 49,
    "Hatchet": 50, "Leatherworking": 51, "Cloth Tailoring": 52, "Masonry": 53,
    "Blades Smithing": 54, "Weapon Heads Smithing": 55, "Chain Armour Smithing": 56,
    "Plate Armour Smithing": 57, "Shield Smithing": 58, "Blacksmithing": 59,
    "Dairy Food Making": 60, "Hot Food Cooking": 61, "Baking": 62, "Beverages": 63,
    "Longsword": 64, "Large Maul": 65, "Medium Maul": 66, "Small Maul": 67,
    "Warhammer": 68, "Long spear": 69, "Halberd": 70, "Staff": 71,
    "Carving Knife": 72, "Butchering Knife": 73, "Stone Chisel": 74,
    "Huge Club": 75, "Saw": 76, "Butchering": 77, "Carpentry": 78,
    "Firemaking": 79, "Tracking": 80, "Small Wooden Shield": 81,
    "Medium Wooden Shield": 82, "Large Wooden Shield": 83, "Small Metal Shield": 84,
    "Large Metal Shield": 85, "Medium Metal Shield": 86, "Large Axe": 87,
    "Huge Axe": 88, "Shortsword": 89, "Two Handed Sword": 90, "Hammer": 91,
    "Paving": 92, "Prospecting": 93, "Fishing": 94, "Locksmithing": 95,
    "Repairing": 96, "Coal-Making": 97, "Milling": 98, "Metallurgy": 99,
    "Natural Substances": 100, "Jewelry Smithing": 101, "Fine Carpentry": 102,
    "Bowyery": 103, "Fletching": 104, "Yoyo": 105, "Puppeteering": 106,
    "Toy Making": 107, "Weaponless Fighting": 108, "Aggressive Fighting": 109,
    "Defensive Fighting": 110, "Normal Fighting": 111, "First Aid": 112,
    "Taunting": 113, "Shield Bashing": 114, "Milking": 115, "Preaching": 116,
    "Prayer": 117, "Channeling": 118, "Exorcism": 119, "Archaeology": 120,
    "Foraging": 121, "Botanizing": 122, "Climbing": 123, "Stone Cutting": 124,
    "Lock Picking": 125, "Stealing": 126, "Traps": 127, "Catapults": 128,
    "Animal Taming": 129, "Animal Husbandry": 130, "Short Bow": 131,
    "Long Bow": 132, "Medium Bow": 133, "Ship Building": 134, "Ballistae": 135,
    "Trebuchets": 136, "Restoration": 137
}
skill_names = sorted(list(skill_map.keys()))

# --- Interface da Aplicação Web ---

# Título da página
st.set_page_config(page_title="Calculadora Taste Food", page_icon="🍺")
st.title("🍺 Calculadora de Bebida para Skill")
st.write("Uma ferramenta para uso da Fortaleza das Cinzas para calcular a bebida necessária para obter uma skill específica a partir da Taste Food.")

# Seleção da Skill Atual
st.header("🍔 Skill da Taste Food:")
skill_atual_nome = st.selectbox(
    "Selecione ou digite a skill que você obteve com a Taste Food:",
    options=skill_names,
    index=None,  # Começa sem nada selecionado
    placeholder="Escolha uma skill..."
)

# Seleção da Skill Desejada
st.header("🎖️ Skill Desejada:")
skill_desejada_nome = st.selectbox(
    "Selecione ou digite a skill que você deseja:",
    options=skill_names,
    index=None,
    placeholder="Escolha uma skill..."
)

# Botão de Cálculo e Lógica
if st.button("🧮 Calcular Bebida", type="primary"):
    if skill_atual_nome and skill_desejada_nome:
        try:
            skill_atual = skill_map[skill_atual_nome]
            skill_desejada = skill_map[skill_desejada_nome]

            # Cálculo da bebida (mesma lógica sua)
            valor_player = skill_atual - 37
            if valor_player < 0:
                valor_player += 138

            numero_bebida = skill_desejada - valor_player
            if numero_bebida < 0:
                numero_bebida += 138
            
            if numero_bebida >= 138:
                numero_bebida -= 138

            # Exibe o resultado com sucesso
            st.success(f"## 🍷 Bebida Necessária: Nº {numero_bebida}")
            st.info(f"**Caminho:** `{skill_atual_nome}` → `{skill_desejada_nome}`")

        except Exception as e:
            st.error(f"Ocorreu um erro inesperado: {e}")
    else:
        # Avisa se algum campo estiver vazio
        st.warning("⚠️ Por favor, selecione ambas as skills para calcular.")

st.markdown("---")
st.write("Feito com 💙 por Skinbro em colaboração com a Fortaleza das Cinzas 🏰.")
