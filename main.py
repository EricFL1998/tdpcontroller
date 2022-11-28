class Plugin:
        # The backend function that we called above
    async def change_tdp(watts):
        power = watts *1000
        ./backend/ryzenadj --stapm-limit=$power --fast-limit=$power --slow-limit=$power

        # Function that can contain long-running code that will stay alive for the entire duration of your plugin
    #async def _main(self):
       # pass

     # Function used to clean up a plugin when it's told to unload by Decky-Loader
    #async def _unload(self):
     #   pass