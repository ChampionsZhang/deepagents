"""Built-in Claude Opus 5 harness profile.

Adds concise scope and delegation steering for Claude Opus 5. No separate
verification overlay is added: Anthropic documents that Opus 5 verifies its
own work and that added verification scaffolding costs tokens without
improving quality. The universal `tool_result_reflection` section is still
inherited, since Anthropic publishes it as cross-model guidance and does not
carve Opus 5 out of it; if a future revision does, drop that section here.

Source: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5
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
<response_style>
Keep responses focused and reasonably concise. Lead with the outcome, keep caveats brief, and match written deliverable length to the substance of the task without filler or redundant summaries.
</response_style>

<task_scope>
Deliver what was asked at the intended scope. Make routine judgment calls yourself, but do not quietly narrow, widen, or transform the request. Finish the task and stop short of actions clearly beyond it.
</task_scope>

<subagent_usage>
Delegate only large, genuinely independent work that benefits from parallel execution. Do not delegate work you can finish in a handful of tool calls, do not use subagents merely to verify your own work, and keep the number of subagents low.
</subagent_usage>"""
"""Claude Opus 5-specific guidance appended after the universal sections."""

_SYSTEM_PROMPT_SUFFIX = _claude_guidance_with_overlay(_MODEL_SPECIFIC_OVERLAY)
"""Text appended to the assembled base system prompt."""


def register() -> None:
    """Register the built-in Claude Opus 5 harness profile."""
    _register_harness_profile_impl(
        "anthropic:claude-opus-5",
        HarnessProfile(system_prompt_suffix=_SYSTEM_PROMPT_SUFFIX),
    )
