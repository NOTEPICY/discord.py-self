# discord_protos.py

# This is a dummy fallback implementation of PreloadedUserSettings
# used to prevent ModuleNotFoundError in patched versions of discord.py-self.

class PreloadedUserSettings:
    def __init__(self):
        self.guild_positions = []
        self.guild_folders = []
        self.detection_status = None
        self.theme = "dark"
        self.developer_mode = True
        self.locale = "en-US"
        self.render_embeds = True
        self.message_display_compact = False
        self.inline_embed_media = True
        self.inline_attachment_media = True
        self.animate_emoji = True
        self.animate_stickers = 1
        self.render_reactions = True
        self.disable_gifs = False
        self.explicit_content_filter = 2
        self.friend_source_flags = {
            "all": True,
            "mutual_guilds": True,
            "mutual_friends": True
        }
        self.status = "online"
        self.detect_platform_accounts = False
        self.afk_timeout = 300
        self.allow_accessibility_detection = False
        self.contact_sync_enabled = False
        self.convert_emoticons = True
        self.enable_tts_command = False
        self.default_guilds_restricted = False
        self.view_nsfw_guilds = True
        self.guild_positions = []
        self.native_phone_integration_enabled = False
        self.restricted_guilds = []
        self.passwordless = False
        self.profile = {}

    def SerializeToString(self):
        return b""