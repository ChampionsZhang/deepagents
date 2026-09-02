"""Built-in Claude Sonnet 5 harness profile.

Adds minimal scope guidance for Sonnet 5's more literal instruction
following.

Deliberately omitted from the published guidance: thinking, effort, sampling,
and `max_tokens` recommendations are API-level and belong to model
construction rather than the harness prompt. Verbosity calibration is left
alone because Sonnet 5 scales response length to task complexity on its own,
and the thinking-disabled tool-use nudge does not apply — Sonnet 5 runs with
adaptive thinking on by default. Add either one here if a caller-visible
behavior turns up that the harness should steer.

Source: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5
"""

# ruff: noqa: E501
# Prompt sections are single lines by design so source wrapping does not
# alter the guidance injected into the system prompt.

from deepagents.profiles.harness._anthropic import (
    _claude_guidance_with_overlay,
)
from deepagents.profiles.harness.harness_profiles import (
    HarnessProfile,
    _register_harness_profile_impl,
)

_MODEL_SPECIFIC_OVERLAY = """\
<instruction_scope>
Follow the user's explicit scope literally. When an instruction applies to a collection or the whole task, apply it to every relevant item, not only the first. Do not infer requests the user did not make.
</instruction_scope>"""
"""Claude Sonnet 5-specific guidance appended after the universal sections."""

_SYSTEM_PROMPT_SUFFIX = _claude_guidance_with_overlay(_MODEL_SPECIFIC_OVERLAY)
"""Text appended to the assembled base system prompt."""


def register() -> None:
    """Register the built-in Claude Sonnet 5 harness profile."""
    _register_harness_profile_impl(
        "anthropic:claude-sonnet-5",
        HarnessProfile(system_prompt_suffix=_SYSTEM_PROMPT_SUFFIX),
    )
