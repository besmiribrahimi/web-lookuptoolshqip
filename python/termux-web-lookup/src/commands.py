from search import SearchEngine
from ui import format_results, format_error

class CommandHandler:
    
    def __init__(self):
        self.search_engine = SearchEngine()
        self.commands = {
            'search': self.cmd_search,
            'google': self.cmd_google,
            'duckduckgo': self.cmd_duckduckgo,
            'define': self.cmd_define,
            'help': self.cmd_help,
            'exit': self.cmd_exit,
            'quit': self.cmd_exit,
        }
    
    def handle(self, user_input, console):
        parts = user_input.strip().split(maxsplit=1)
        
        if not parts:
            return
        
        command = parts[0].lower()
        args = parts[1] if len(parts) > 1 else ""
        
        if command in self.commands:
            self.commands[command](args, console)
        else:
            format_error(console, f"Komanda e panjohur: {command}")
    
    def cmd_search(self, query, console):
        if not query:
            format_error(console, "Përdorimi: search <pyetje>")
            return
        
        console.print(f"[yellow]Po kërkojmë për: {query}[/yellow]")
        results = self.search_engine.search(query, engine='google')
        format_results(console, results, query)
    
    def cmd_google(self, query, console):
        if not query:
            format_error(console, "Përdorimi: google <pyetje>")
            return
        
        console.print(f"[yellow]Po kërkojmë në Google për: {query}[/yellow]")
        results = self.search_engine.search(query, engine='google')
        format_results(console, results, query)
    
    def cmd_duckduckgo(self, query, console):
        if not query:
            format_error(console, "Përdorimi: duckduckgo <pyetje>")
            return
        
        console.print(f"[yellow]Po kërkojmë në DuckDuckGo për: {query}[/yellow]")
        results = self.search_engine.search(query, engine='duckduckgo')
        format_results(console, results, query)
    
    def cmd_define(self, word, console):
        if not word:
            format_error(console, "Përdorimi: define <fjalë>")
            return
        
        console.print(f"[yellow]Po kërkojmë përkufizimin për: {word}[/yellow]")
        console.print("[dim]Veçori do të vjet më shpejti...[/dim]")
    
    def cmd_help(self, args, console):
        from ui import display_help
        display_help(console)
    
    def cmd_exit(self, args, console):
        console.print("[green]Mirupafshim![/green]")
        exit(0)
