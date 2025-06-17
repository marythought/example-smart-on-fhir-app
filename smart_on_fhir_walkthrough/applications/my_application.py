from urllib.parse import urlencode

from canvas_sdk.effects import Effect
from canvas_sdk.effects.launch_modal import LaunchModalEffect
from canvas_sdk.handlers.application import Application


class MyApplication(Application):
    """An embeddable application that can be registered to Canvas."""

    def on_open(self) -> Effect:
        """Handle the on_open event."""

        launch_params = {
            "iss": f"https://fumage-{self.environment['CUSTOMER_IDENTIFIER']}.canvasmedical.com",
            "aud": f"https://fumage-{self.environment['CUSTOMER_IDENTIFIER']}.canvasmedical.com",
            "launch": self.context["patient"]["id"]
        }

        encoded_launch_params = urlencode(launch_params)

        # Implement this method to handle the application on_open event.
        return LaunchModalEffect(
            url=f"https://marythought.github.io/example-smart-on-fhir-app//launch.html?{encoded_launch_params}",
            target=LaunchModalEffect.TargetType.RIGHT_CHART_PANE,
        ).apply()
