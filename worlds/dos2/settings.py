import os

import settings


class DOS2Settings(settings.Group):
    class RootDirectory(settings.UserFolderPath):
        """
        Locates the DOS2 root directory on your system.
        This is used by the client, so it knows where to save and read from DOS2
        """

        description = "DOS2 root directory"

        def browse(self, **kwargs):
            from Utils import messagebox

            messagebox(
                "DOS2 folder not found",
                "DOS2Client couldn't find a path to the DOS2 folder.\nPlease select the DOS2 install folder",
            )
            return super().browse(**kwargs)

    root_directory: RootDirectory = RootDirectory(
        os.path.join("Documents", "Larian Studios", "Divinity Original Sin 2 Definitive Edition", "Osiris Data")
    )
