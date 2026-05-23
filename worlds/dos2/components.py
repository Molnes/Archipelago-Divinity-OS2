from worlds.LauncherComponents import Component, Type, components, launch


def run_client(*args: str) -> None:
    from .client import launch_dos2_client

    launch(launch_dos2_client, name="Divinity: Original Sin 2 Client", args=args)


components.append(
    Component(
        "Divinity: Original Sin 2 Client",
        func=run_client,
        game_name="Divinity: Original Sin 2",
        component_type=Type.CLIENT,
        supports_uri=True,
    )
)
