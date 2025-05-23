import time

def print_seal():                                                                                                  
    print("██████████████████████████████▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒░▒▒▒▒▒▓▓▒▓▓▓▒▓▓█████████████")
    print("███████████████████████████▓▒▒▒▒▒▓▓▓▓▓▓▓▓▓▒▒▒▒▒░░░░░ ░░░▒▒▒▒▒▒▒▒▒▒▓░▒██████████")
    print("████████████████████████▓▓▒░▒▒▒▓█▓▓▓▓▓▒▒▒▒▒░░▒░░░░░░░░░░▒▒▓░░▒▒▒▒▒░░▓▓█████████")
    print("██████████████████████▓▒▒░▒▒▒▓▓▓▒░░░░░░░░▒░░░░░░░▒▒▒▒▒▒▒░░░██ ░ ▓▒░░▒▓██▓██████")
    print("█████████████████████▒▒▒▒▒▒▒▓▓▒░ ░░░▓██▒░░░░░░░▒▒▒▒▒▒▒░░░░░░░▒░░▒▒▒▓███████████")
    print("███████████████████▒▒▒▒▒▒▒▓▓▒▒░░░░░░░░█▓░░░░░▒▒▒▒▒▒▒▒▒▒░░░░░░▒▓▒▓▓▓▓▓▒██▓██████")
    print("██████████████████▒▒▒▒▒▒░▒▓▓▒░   ░░░▒▒▓▒░░░░▒▒▓▓▓█▓▓▓▓▒▓░▓▓█▓█▓▓███████▒███████")
    print("█████████████████▒▒▒▒▒▒▒▒▒▓▒▒▒░       ░░░░▒▒▒▒▒▒▒▒▒▓▒▓▓▓▒▓█████▓▓▒▒▓▓███▓██████")
    print("███████████████▓▒▒▒▒░▒▒▒░▒▒▓▓▒▒░░  ░░▒░░▒░▒▒▓▒▓▒▒▒▒▒░▒▒▒█▓███▒░░░░░   ▒█▓██████")
    print("██████████████▒▒▒▒▒▒░░░░░▒▒▓▓▓▓▒░░  ░░░░░▒▒░░░▒░▒▒▒░▒▒▒▒██▓▒░░░░░░    ░█▓██████")
    print("█████████████▒▒▒▒▒░░░░░▒▒▒▒▒▒▒▒▒▒░░░░░░░▒▒░▒░▒▒░░░░▒▒▓▓█▓░░░░░░░░     ▒████████")
    print("███████████▓▒░▒▒░░▒░░░░▒▒▓▒▒▓▒▒░░░░░░░  ░▒▒░▒▒░░░▒▒▒▓█▓░░░░░░░░░░░    ▓████████")
    print("██████████▓▒▒▒▒░░░░░░░▒▒▒▒▒▓▒▒▒▒▒▒░░░       ░▒░░▒▒▓▓▓░░░░░▒▒▒░░░░    ░█████████")
    print("████████▓▒▒░▒▒░▒░░░░░░░▒▒░░▒▒▒▒▒▒▒▒▒░░░▒░░░ ░░░▒▒▒▒▓▒▒▒░▒░░░░░░░▒░   ░█████████")
    print("███████▒░▒░▒░░░░░░░░░░░░░░▒▒░▒▓▒▒▒▒▒▒░░▒▒▒▒░░░░▒▒▒▒▒░░░░░░░░░░░░░░   ░█████████")
    print("████▓▓▒░░▒▒▒░░░░░░░░░░░░░░░░░▒▒▒░▓▒▓▓▓▓▒▓▓▒▒░░░▒▒▒▒▒░░░░░░░░░░░░░░░  ▒█████████")
    print("    __  __    _    _____    ____    _    ____  ____ _____ ___  _   _ _____     ")
    print("   |  \/  |  / \  | ____|  / ___|  / \  |  _ \/ ___|_   _/ _ \| \ | | ____|    ")
    print("   | |\/| | / _ \ |  _|   | |     / _ \ | |_) \___ \ | || | | |  \| |  _|      ")
    print("   | |  | |/ ___ \| |___  | |___ / ___ \|  __/ ___) || || |_| | |\  | |___     ")
    print("   |_|  |_/_/   \_\_____|  \____/_/   \_\_|   |____/ |_| \___/|_| \_|_____|    ")
    
    
def get_time_millis(start_time):
    """Calculate elapsed time since start_time."""
    elapsed_time = time.time() - start_time
    
    return elapsed_time * 1000  # Convert to milliseconds
