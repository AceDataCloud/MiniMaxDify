"""Published API contracts; source revisions are recorded in tests/parity-audit.json."""

TASK_PATH = "/minimax/tasks"

ENDPOINTS = {
    "minimax_generate_video": {
        "method": "POST",
        "path": "/minimax/videos",
        "operation": "generate",
        "schema": {
            "type": "object",
            "additionalProperties": False,
            "required": ["model", "content", "resolution", "duration"],
            "properties": {
                "model": {"type": "string", "enum": ["MiniMax-H3"]},
                "content": {
                    "type": "array",
                    "minItems": 1,
                    "items": {
                        "oneOf": [
                            {
                                "type": "object",
                                "additionalProperties": False,
                                "required": ["type", "text"],
                                "properties": {
                                    "type": {"type": "string", "enum": ["text"]},
                                    "text": {"type": "string", "minLength": 1, "maxLength": 7000},
                                },
                            },
                            {
                                "type": "object",
                                "additionalProperties": False,
                                "required": ["type", "image_url"],
                                "properties": {
                                    "type": {"type": "string", "enum": ["image_url"]},
                                    "image_url": {
                                        "type": "object",
                                        "additionalProperties": False,
                                        "required": ["url"],
                                        "properties": {"url": {"type": "string"}},
                                    },
                                    "role": {
                                        "type": "string",
                                        "enum": ["first_frame", "last_frame", "reference_image"],
                                    },
                                },
                            },
                            {
                                "type": "object",
                                "additionalProperties": False,
                                "required": ["type", "video_url", "role"],
                                "properties": {
                                    "type": {"type": "string", "enum": ["video_url"]},
                                    "video_url": {
                                        "type": "object",
                                        "additionalProperties": False,
                                        "required": ["url"],
                                        "properties": {"url": {"type": "string"}},
                                    },
                                    "role": {"type": "string", "enum": ["reference_video"]},
                                },
                            },
                            {
                                "type": "object",
                                "additionalProperties": False,
                                "required": ["type", "audio_url", "role"],
                                "properties": {
                                    "type": {"type": "string", "enum": ["audio_url"]},
                                    "audio_url": {
                                        "type": "object",
                                        "additionalProperties": False,
                                        "required": ["url"],
                                        "properties": {"url": {"type": "string"}},
                                    },
                                    "role": {"type": "string", "enum": ["reference_audio"]},
                                },
                            },
                        ]
                    },
                },
                "resolution": {"type": "string", "enum": ["480P", "768P", "2K"]},
                "duration": {"type": "integer", "minimum": 4, "maximum": 15},
                "ratio": {
                    "type": "string",
                    "enum": ["adaptive", "21:9", "16:9", "4:3", "1:1", "3:4", "9:16"],
                },
                "callback_url": {"type": "string", "format": "uri"},
                "async": {"type": "boolean"},
            },
        },
        "properties": {
            "model": {"type": "string", "enum": ["MiniMax-H3"]},
            "content": {
                "type": "array",
                "minItems": 1,
                "items": {
                    "oneOf": [
                        {
                            "type": "object",
                            "additionalProperties": False,
                            "required": ["type", "text"],
                            "properties": {
                                "type": {"type": "string", "enum": ["text"]},
                                "text": {"type": "string", "minLength": 1, "maxLength": 7000},
                            },
                        },
                        {
                            "type": "object",
                            "additionalProperties": False,
                            "required": ["type", "image_url"],
                            "properties": {
                                "type": {"type": "string", "enum": ["image_url"]},
                                "image_url": {
                                    "type": "object",
                                    "additionalProperties": False,
                                    "required": ["url"],
                                    "properties": {"url": {"type": "string"}},
                                },
                                "role": {
                                    "type": "string",
                                    "enum": ["first_frame", "last_frame", "reference_image"],
                                },
                            },
                        },
                        {
                            "type": "object",
                            "additionalProperties": False,
                            "required": ["type", "video_url", "role"],
                            "properties": {
                                "type": {"type": "string", "enum": ["video_url"]},
                                "video_url": {
                                    "type": "object",
                                    "additionalProperties": False,
                                    "required": ["url"],
                                    "properties": {"url": {"type": "string"}},
                                },
                                "role": {"type": "string", "enum": ["reference_video"]},
                            },
                        },
                        {
                            "type": "object",
                            "additionalProperties": False,
                            "required": ["type", "audio_url", "role"],
                            "properties": {
                                "type": {"type": "string", "enum": ["audio_url"]},
                                "audio_url": {
                                    "type": "object",
                                    "additionalProperties": False,
                                    "required": ["url"],
                                    "properties": {"url": {"type": "string"}},
                                },
                                "role": {"type": "string", "enum": ["reference_audio"]},
                            },
                        },
                    ]
                },
            },
            "resolution": {"type": "string", "enum": ["480P", "768P", "2K"]},
            "duration": {"type": "integer", "minimum": 4, "maximum": 15},
            "ratio": {
                "type": "string",
                "enum": ["adaptive", "21:9", "16:9", "4:3", "1:1", "3:4", "9:16"],
            },
            "callback_url": {"type": "string", "format": "uri"},
            "async": {"type": "boolean"},
        },
        "parameters": [],
        "defaults": {"model": "MiniMax-H3", "resolution": "768P", "duration": 4, "ratio": "16:9"},
        "fixed": {},
        "allow_empty": [],
        "query_actions": [],
        "media_response": False,
    },
    "minimax_list_tasks": {
        "method": "POST",
        "path": "/minimax/tasks",
        "operation": "request",
        "schema": {
            "type": "object",
            "properties": {
                "action": {"type": "string", "enum": ["retrieve", "retrieve_batch", "delete"]},
                "id": {"type": "string"},
                "ids": {"type": "array", "items": {"type": "string"}},
                "limit": {"type": "integer"},
                "offset": {"type": "integer"},
                "created_at_min": {"type": "number"},
                "created_at_max": {"type": "number"},
            },
        },
        "properties": {
            "action": {"type": "string", "enum": ["retrieve", "retrieve_batch", "delete"]},
            "id": {"type": "string"},
            "ids": {"type": "array", "items": {"type": "string"}},
            "limit": {"type": "integer"},
            "offset": {"type": "integer"},
            "created_at_min": {"type": "number"},
            "created_at_max": {"type": "number"},
        },
        "parameters": [],
        "defaults": {"action": "retrieve"},
        "fixed": {},
        "allow_empty": [],
        "query_actions": ["retrieve", "retrieve_batch", "list", "presets"],
        "media_response": False,
    },
    "minimax_delete_task": {
        "method": "POST",
        "path": "/minimax/tasks",
        "operation": "request",
        "schema": {
            "type": "object",
            "properties": {
                "action": {"type": "string", "enum": ["retrieve", "retrieve_batch", "delete"]},
                "id": {"type": "string"},
                "ids": {"type": "array", "items": {"type": "string"}},
                "limit": {"type": "integer"},
                "offset": {"type": "integer"},
                "created_at_min": {"type": "number"},
                "created_at_max": {"type": "number"},
            },
        },
        "properties": {
            "action": {"type": "string", "enum": ["retrieve", "retrieve_batch", "delete"]},
            "id": {"type": "string"},
            "ids": {"type": "array", "items": {"type": "string"}},
            "limit": {"type": "integer"},
            "offset": {"type": "integer"},
            "created_at_min": {"type": "number"},
            "created_at_max": {"type": "number"},
        },
        "parameters": [],
        "defaults": {"action": "delete"},
        "fixed": {"action": "delete"},
        "allow_empty": [],
        "query_actions": ["retrieve", "retrieve_batch", "list", "presets"],
        "media_response": False,
        "destructive": True,
    },
    "minimax_task_retrieve": {
        "method": "POST",
        "path": "/minimax/tasks",
        "operation": "task",
        "schema": {
            "type": "object",
            "properties": {
                "action": {"type": "string", "enum": ["retrieve", "retrieve_batch", "delete"]},
                "id": {"type": "string"},
                "ids": {"type": "array", "items": {"type": "string"}},
                "limit": {"type": "integer"},
                "offset": {"type": "integer"},
                "created_at_min": {"type": "number"},
                "created_at_max": {"type": "number"},
            },
        },
        "properties": {
            "action": {"type": "string", "enum": ["retrieve", "retrieve_batch", "delete"]},
            "id": {"type": "string"},
            "ids": {"type": "array", "items": {"type": "string"}},
            "limit": {"type": "integer"},
            "offset": {"type": "integer"},
            "created_at_min": {"type": "number"},
            "created_at_max": {"type": "number"},
        },
        "parameters": [],
        "defaults": {"wait_seconds": 0},
        "fixed": {},
        "allow_empty": [],
        "query_actions": ["retrieve", "retrieve_batch", "list", "presets"],
        "media_response": False,
    },
    "minimax_tasks_retrieve_batch": {
        "method": "POST",
        "path": "/minimax/tasks",
        "operation": "batch",
        "schema": {
            "type": "object",
            "properties": {
                "action": {"type": "string", "enum": ["retrieve", "retrieve_batch", "delete"]},
                "id": {"type": "string"},
                "ids": {"type": "array", "items": {"type": "string"}, "minItems": 1},
                "limit": {"type": "integer"},
                "offset": {"type": "integer"},
                "created_at_min": {"type": "number"},
                "created_at_max": {"type": "number"},
            },
            "required": ["action", "ids"],
        },
        "properties": {
            "action": {"type": "string", "enum": ["retrieve", "retrieve_batch", "delete"]},
            "id": {"type": "string"},
            "ids": {"type": "array", "items": {"type": "string"}, "minItems": 1},
            "limit": {"type": "integer"},
            "offset": {"type": "integer"},
            "created_at_min": {"type": "number"},
            "created_at_max": {"type": "number"},
        },
        "parameters": [],
        "defaults": {},
        "fixed": {"action": "retrieve_batch"},
        "allow_empty": [],
        "query_actions": ["retrieve", "retrieve_batch", "list", "presets"],
        "media_response": False,
    },
}
