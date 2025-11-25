import generator
import saved

def main():
    print("Генератор тайлсетов WinMax2025")
    
    while True:
        print("\nВыберите палитру:")
        print("1 - океан")
        print("2 - пустыня") 
        print("3 - лес")
        print("4 - город")
        print("5 - пляж")
        print("6 - ледник")
        print("7 - горы")
        print("8 - пещера")
        print("9 - болото")
        
        try:
            palette_choice = int(input("Ваш выбор: "))
            palettes = {
                1: "океан", 2: "пустыня", 3: "лес", 4: "город", 
                5: "пляж", 6: "ледник", 7: "горы", 8: "пещера", 9: "болото"
            }
            palette = palettes[palette_choice]
            print(f"Выбрана палитра: {palette}")
            break
        except (ValueError, KeyError):
            print("Ошибка: выберите число от 1 до 9")
    
    while True:
        print("\nВыберите размер тайла:")
        print("1 - 8x8")
        print("2 - 16x16")
        print("3 - 32x32")
        
        try:
            size_choice = int(input("Ваш выбор: "))
            sizes = {1: 8, 2: 16, 3: 32}
            tile_size = sizes[size_choice]
            print(f"Выбран размер: {tile_size}x{tile_size}")
            break
        except (ValueError, KeyError):
            print("Ошибка: выберите число от 1 до 3")
    
    while True:
        print("\nВыберите уровень детализации:")
        print("1 - низкий")
        print("2 - средний")
        print("3 - высокий")
        
        try:
            detail_choice = int(input("Ваш выбор: "))
            details = {1: "низкий", 2: "средний", 3: "высокий"}
            detail_level = details[detail_choice]
            print(f"Выбрана детализация: {detail_level}")
            break
        except (ValueError, KeyError):
            print("Ошибка: выберите число от 1 до 3")

    tileset = generator.generate_tileset(
        rows=3,
        cols=3, 
        tile_size=tile_size,
        palette_name=palette,
        detail_level=detail_level
    )
    saved.save_tileset(tileset)

if __name__ == "__main__":
    main()
