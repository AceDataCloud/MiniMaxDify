# MiniMax H3 capability mapping

Compared with [MCPs at f0eed10abf31](https://github.com/AceDataCloud/MCPs/tree/f0eed10abf310824cb4c33d4944c63d3654ac95b/minimax) and the public API contract at PlatformBackend `fa94598267a82545fb1afed6ee26bafd6cbb9ca7`.

The table maps service operations to Dify tools. Different MCP helper functions may use the same action selector or structured JSON input.

| MCP function | Dify equivalent | Notes |
|---|---|---|
| `minimax_list_models` |  | Model/action selectors and the API reference; informational guidance does not submit a request. |
| `minimax_list_actions` |  | Model/action selectors and the API reference; informational guidance does not submit a request. |
| `minimax_list_tasks` | `minimax_list_tasks` | Set action=retrieve |
| `minimax_get_task` | `minimax_task_retrieve` | Set action=retrieve |
| `minimax_get_tasks_batch` | `minimax_tasks_retrieve_batch` | Set action=retrieve_batch |
| `minimax_delete_task` | `minimax_task_retrieve` | Set action=delete |
| `minimax_generate_video_from_text` | `minimax_generate_video` |  |
| `minimax_generate_video_from_images` | `minimax_generate_video` |  |
| `minimax_generate_video_from_audio` | `minimax_generate_video` |  |
| `minimax_generate_video` | `minimax_generate_video` |  |

## Parameter equivalents

- `minimax_get_tasks_batch`: `task_ids` → ids.
- `minimax_generate_video_from_text`: `prompt` → content[] entries (text, image_url or audio_url), `async_` → Dify submit/poll output: async=true, stream=false.
- `minimax_generate_video_from_images`: `image_urls` → content[] entries (text, image_url or audio_url), `prompt` → content[] entries (text, image_url or audio_url), `async_` → Dify submit/poll output: async=true, stream=false.
- `minimax_generate_video_from_audio`: `audio_urls` → content[] entries (text, image_url or audio_url), `image_urls` → content[] entries (text, image_url or audio_url), `prompt` → content[] entries (text, image_url or audio_url), `async_` → Dify submit/poll output: async=true, stream=false.
- `minimax_generate_video`: `async_` → Dify submit/poll output: async=true, stream=false.

## Verification boundary

Contract examples and regression tests cover request validation, transport and task handling. Actual Dify browser cases are recorded separately in `tests/e2e-results.json` and `tests/e2e-audit.json` when available. A schema test is not a successful paid generation. Unsupported service availability and untested advanced combinations must not be described as passed.
