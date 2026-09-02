"""Built-in Claude Haiku 4.5 harness profile.

Layers Anthropic's universal Claude guidance onto
`anthropic:claude-haiku-4-5` — parallel tool calls, grounded (non-
speculative) answers, and post-tool-result reflection.

No Claude-Haiku-4.5-specific overlays. Anthropic's published prompting
guide does not carve out Haiku 4.5 for dedicated prompt steering; the
only Haiku-specific call-outs concern API-level capabilities
(context-window awareness) rather than system-prompt content, and the
overeagerness / overthinking / subagent-overuse snippets are tagged
for Claude Opus 4.5 / Claude Opus 4.6 and do not apply to Haiku 4.5.
This module exists as the audit anchor: its presence documents the
review and justifies the absence of model-specific prompt content. If
a future revision of the prompting guide adds Haiku-4.5-specific
guidance, add it here rather than at the provider key so it does not
leak onto other Anthropic models.

Source: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
"""

from deepagents.profiles.harness._anthropic import _UNIVERSAL_CLAUDE_GUIDANCE
from deepagents.profiles.harness.harness_profiles import (
    HarnessProfile,
    _register_harness_profile_impl,
)

_SYSTEM_PROMPT_SUFFIX = _UNIVERSAL_CLAUDE_GUIDANCE
"""Text appended to the assembled base system prompt."""


def register() -> None:
    """Register the built-in Claude Haiku 4.5 harness profile."""
    _register_harness_profile_impl(
        "anthropic:claude-haiku-4-5",
        HarnessProfile(system_prompt_suffix=_SYSTEM_PROMPT_SUFFIX),
    )
