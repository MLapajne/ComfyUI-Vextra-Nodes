import subprocess, sys, os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

# Set the SDL audio driver to dummy to avoid issues with missing audio hardware
os.environ['SDL_AUDIODRIVER'] = 'dummy'

try:
    from pygame import mixer
except ModuleNotFoundError:
    # install pixelsort in current venv
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame"])
    from pygame import mixer

try:
    mixer.init()
except pygame.error as e:
    print(f"Audio initialization failed: {e}")

def PlaySound(path, volume):
    try:
        mixer.music.load(path)
        mixer.music.set_volume(volume)
        mixer.music.play()
    except Exception as e:
        print(f"Error playing sound: {e}")

class Play_Sound_RealTime():
    """
    This node provides a simple interface to apply PixelSort blur to the output image.
    """
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        """
        Input Types
        """
        return {
            "required": {
                "images": ("IMAGE",),
                "path": ("STRING", {"default": 'change_me.mp3'}),
                "volume": ("FLOAT", {"default": 1, "min": 0.0, "max": 1.0, "step": 0.01}),
                },
            "optional": {
                },
            }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "do_sound"
    
    OUTPUT_NODE = True

    CATEGORY = "VextraNodes"

    def do_sound(self, images, path, volume):
        PlaySound(path, volume)
        return {
            "result": (images, ),
        }

NODE_CLASS_MAPPINGS = {
    "Play Sound At Execution": Play_Sound_RealTime
}
