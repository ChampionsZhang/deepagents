"""Built-in Claude Sonnet 4.6 harness profile.

Layers Anthropic's universal Claude guidance onto
`anthropic:claude-sonnet-4-6` — parallel tool calls, grounded (non-
speculative) answers, and post-tool-result reflection.

No Claude-Sonnet-4.6-specific overlays. Anthropic's published guidance
for Sonnet 4.6 centers on API-level configuration (effort defaults,
adaptive thinking, `budget_tokens` deprecation) rather than system-
prompt adjustments; the overeagerness, overthinking, and subagent-
overuse prompt snippets in the guide are tagged for Claude Opus 4.5 /
Claude Opus 4.6 and do not apply to Sonnet 4.6. This module exists as
the audit anchor: its presence documents the review and justifies the
absence of model-specific prompt content. If a future revision of the
prompting guide adds Sonnet-4.6-specific guidance, add it here rather
than at the provider key so it does not leak onto other Anthropic
models.

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
    """Register the built-in Claude Sonnet 4.6 harness profile."""
    _register_harness_profile_impl(
        "anthropic:claude-sonnet-4-6",
        HarnessProfile(system_prompt_suffix=_SYSTEM_PROMPT_SUFFIX),
    )
