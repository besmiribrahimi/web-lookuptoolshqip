from rich.console import Console
from rich.prompt import Prompt
from commands import CommandHandler
from ui import display_welcome, display_help

console = Console()

def main():
    cmd_handler = CommandHandler()
    
    display_welcome(console)
    display_help(console)
    
    try:
        while True:
            try:
                user_input = Prompt.ask("[cyan]termux-lookup[/cyan]")
                
                if not user_input.strip():
                    continue
                
                cmd_handler.handle(user_input, console)
                
            except KeyboardInterrupt:
                console.print("\n[yellow]U ndërpre[/yellow]")
                continue
                
    except EOFError:
        console.print("[green]Mirupafshim![/green]")

if __name__ == "__main__":
    main()
