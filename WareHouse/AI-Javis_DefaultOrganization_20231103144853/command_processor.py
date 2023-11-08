'''
This file handles processing of voice commands.
'''
class CommandProcessor:
    def __init__(self):
        pass
    def process_command(self, command):
        # Add your command processing logic here
        if command == "hello":
            return "Xin chào!"
        elif command == "what is the weather today":
            return "Hôm nay thời tiết như thế nào?"
        elif command == "play some music":
            return "Phát nhạc cho tôi"
        else:
            return "Lệnh không được hiểu: " + command