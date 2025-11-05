import re
from pathlib import Path


def get_emoji_for_color(color_template):
    theme_emojis = {
        'laranja': '🌙',
        'rosa': '🌸',
        'azul': '💙',
        'verde': '🌿',
        'amarelo': '🌻',
        'roxo': '💜',
    }
    
    if isinstance(color_template, str) and color_template.lower() in theme_emojis:
        return theme_emojis[color_template.lower()]
    
    if isinstance(color_template, str):
        try:
            color_num = int(color_template)
        except ValueError:
            color_num = 208
    else:
        color_num = int(color_template)
    
    if 160 <= color_num <= 220:
        if 160 <= color_num <= 180:
            return '🌹'
        elif 180 <= color_num <= 200:
            return '🌙'
        else:
            return '🌻'
    elif 20 <= color_num <= 50:
        return '💙'
    elif 40 <= color_num <= 85:
        return '🌿'
    elif 90 <= color_num <= 135:
        return '💜'
    else:
        return '✨'


def get_color_mapping(color_template):
    known_themes = {
        'laranja': {
            'DIR_FOREGROUND': 208,
            'DIR_SHORTENED_FOREGROUND': 214,
            'DIR_ANCHOR_FOREGROUND': 220,
            'VCS_CLEAN_FOREGROUND': 172,
            'VCS_UNTRACKED_FOREGROUND': 178,
            'VCS_MODIFIED_FOREGROUND': 208,
            'VCS_VISUAL_IDENTIFIER_COLOR': 211,
            'VCS_LOADING_VISUAL_IDENTIFIER_COLOR': 218,
            'DIRENV_FOREGROUND': 214,
            'PROMPT_CHAR_OK_FOREGROUND': 208,
            'PROMPT_CHAR_ERROR_FOREGROUND': 166,
            'TIME_FOREGROUND': 208,
            'GIT_CLEAN': 208,
            'GIT_MODIFIED': 214,
            'GIT_UNTRACKED': 178,
            'GIT_CONFLICTED': 166,
            'GIT_META': 172,
            'emoji': '🌙',
        },
        'rosa': {
            'DIR_FOREGROUND': 211,
            'DIR_SHORTENED_FOREGROUND': 211,
            'DIR_ANCHOR_FOREGROUND': 218,
            'VCS_CLEAN_FOREGROUND': 217,
            'VCS_UNTRACKED_FOREGROUND': 211,
            'VCS_MODIFIED_FOREGROUND': 218,
            'VCS_VISUAL_IDENTIFIER_COLOR': 211,
            'VCS_LOADING_VISUAL_IDENTIFIER_COLOR': 218,
            'DIRENV_FOREGROUND': 211,
            'PROMPT_CHAR_OK_FOREGROUND': 76,
            'PROMPT_CHAR_ERROR_FOREGROUND': 196,
            'TIME_FOREGROUND': 211,
            'GIT_CLEAN': 217,
            'GIT_MODIFIED': 218,
            'GIT_UNTRACKED': 211,
            'GIT_CONFLICTED': 218,
            'GIT_META': 217,
            'emoji': '🌸',
        },
        'azul': {
            'DIR_FOREGROUND': 39,
            'DIR_SHORTENED_FOREGROUND': 45,
            'DIR_ANCHOR_FOREGROUND': 51,
            'VCS_CLEAN_FOREGROUND': 33,
            'VCS_UNTRACKED_FOREGROUND': 39,
            'VCS_MODIFIED_FOREGROUND': 45,
            'VCS_VISUAL_IDENTIFIER_COLOR': 39,
            'VCS_LOADING_VISUAL_IDENTIFIER_COLOR': 45,
            'DIRENV_FOREGROUND': 39,
            'PROMPT_CHAR_OK_FOREGROUND': 39,
            'PROMPT_CHAR_ERROR_FOREGROUND': 196,
            'TIME_FOREGROUND': 39,
            'GIT_CLEAN': 33,
            'GIT_MODIFIED': 45,
            'GIT_UNTRACKED': 39,
            'GIT_CONFLICTED': 33,
            'GIT_META': 33,
            'emoji': '💙',
        },
        'verde': {
            'DIR_FOREGROUND': 46,
            'DIR_SHORTENED_FOREGROUND': 47,
            'DIR_ANCHOR_FOREGROUND': 48,
            'VCS_CLEAN_FOREGROUND': 42,
            'VCS_UNTRACKED_FOREGROUND': 46,
            'VCS_MODIFIED_FOREGROUND': 47,
            'VCS_VISUAL_IDENTIFIER_COLOR': 46,
            'VCS_LOADING_VISUAL_IDENTIFIER_COLOR': 47,
            'DIRENV_FOREGROUND': 46,
            'PROMPT_CHAR_OK_FOREGROUND': 46,
            'PROMPT_CHAR_ERROR_FOREGROUND': 196,
            'TIME_FOREGROUND': 46,
            'GIT_CLEAN': 42,
            'GIT_MODIFIED': 47,
            'GIT_UNTRACKED': 46,
            'GIT_CONFLICTED': 42,
            'GIT_META': 42,
            'emoji': '🌿',
        },
        'amarelo': {
            'DIR_FOREGROUND': 226,
            'DIR_SHORTENED_FOREGROUND': 227,
            'DIR_ANCHOR_FOREGROUND': 228,
            'VCS_CLEAN_FOREGROUND': 220,
            'VCS_UNTRACKED_FOREGROUND': 226,
            'VCS_MODIFIED_FOREGROUND': 227,
            'VCS_VISUAL_IDENTIFIER_COLOR': 226,
            'VCS_LOADING_VISUAL_IDENTIFIER_COLOR': 227,
            'DIRENV_FOREGROUND': 226,
            'PROMPT_CHAR_OK_FOREGROUND': 226,
            'PROMPT_CHAR_ERROR_FOREGROUND': 196,
            'TIME_FOREGROUND': 226,
            'GIT_CLEAN': 220,
            'GIT_MODIFIED': 227,
            'GIT_UNTRACKED': 226,
            'GIT_CONFLICTED': 220,
            'GIT_META': 220,
            'emoji': '🌻',
        },
        'roxo': {
            'DIR_FOREGROUND': 135,
            'DIR_SHORTENED_FOREGROUND': 141,
            'DIR_ANCHOR_FOREGROUND': 147,
            'VCS_CLEAN_FOREGROUND': 129,
            'VCS_UNTRACKED_FOREGROUND': 135,
            'VCS_MODIFIED_FOREGROUND': 141,
            'VCS_VISUAL_IDENTIFIER_COLOR': 135,
            'VCS_LOADING_VISUAL_IDENTIFIER_COLOR': 141,
            'DIRENV_FOREGROUND': 135,
            'PROMPT_CHAR_OK_FOREGROUND': 135,
            'PROMPT_CHAR_ERROR_FOREGROUND': 196,
            'TIME_FOREGROUND': 135,
            'GIT_CLEAN': 129,
            'GIT_MODIFIED': 141,
            'GIT_UNTRACKED': 135,
            'GIT_CONFLICTED': 129,
            'GIT_META': 129,
            'emoji': '💜',
        },
    }
    
    if isinstance(color_template, str) and color_template.lower() in known_themes:
        mapping = known_themes[color_template.lower()].copy()
        if 'emoji' not in mapping:
            mapping['emoji'] = get_emoji_for_color(color_template)
        return mapping
    
    if isinstance(color_template, str):
        try:
            base_color = int(color_template)
        except ValueError:
            base_color = 208
    else:
        base_color = int(color_template)
    
    vcs_clean = base_color - 36 if base_color >= 36 else base_color + 6
    vcs_modified = base_color
    vcs_untracked = base_color - 30 if base_color >= 30 else base_color
    vcs_conflicted = base_color - 42 if base_color >= 42 else base_color - 6 if base_color >= 6 else base_color
    vcs_meta = base_color - 36 if base_color >= 36 else base_color + 6
    
    mapping = {
        'DIR_FOREGROUND': base_color,
        'DIR_SHORTENED_FOREGROUND': base_color + 6 if base_color < 249 else base_color,
        'DIR_ANCHOR_FOREGROUND': base_color + 12 if base_color < 243 else base_color + 7,
        'VCS_CLEAN_FOREGROUND': vcs_clean,
        'VCS_UNTRACKED_FOREGROUND': vcs_untracked,
        'VCS_MODIFIED_FOREGROUND': vcs_modified,
        'VCS_VISUAL_IDENTIFIER_COLOR': base_color,
        'VCS_LOADING_VISUAL_IDENTIFIER_COLOR': base_color + 7 if base_color < 248 else base_color,
        'DIRENV_FOREGROUND': base_color + 6 if base_color < 249 else base_color,
        'PROMPT_CHAR_OK_FOREGROUND': base_color,
        'PROMPT_CHAR_ERROR_FOREGROUND': 196,
        'TIME_FOREGROUND': base_color,
        'GIT_CLEAN': vcs_clean,
        'GIT_MODIFIED': vcs_modified,
        'GIT_UNTRACKED': vcs_untracked,
        'GIT_CONFLICTED': vcs_conflicted,
        'GIT_META': vcs_meta,
        'emoji': get_emoji_for_color(base_color),
    }
    
    for key, value in mapping.items():
        if key != 'emoji':
            mapping[key] = max(0, min(255, value))
    
    return mapping


def replace_colors_in_content(content, color_mapping):
    patterns = {
        'DIR_FOREGROUND': r'(typeset -g POWERLEVEL9K_DIR_FOREGROUND=)\d+',
        'DIR_SHORTENED_FOREGROUND': r'(typeset -g POWERLEVEL9K_DIR_SHORTENED_FOREGROUND=)\d+',
        'DIR_ANCHOR_FOREGROUND': r'(typeset -g POWERLEVEL9K_DIR_ANCHOR_FOREGROUND=)\d+',
        'VCS_CLEAN_FOREGROUND': r'(typeset -g POWERLEVEL9K_VCS_CLEAN_FOREGROUND=)\d+',
        'VCS_UNTRACKED_FOREGROUND': r'(typeset -g POWERLEVEL9K_VCS_UNTRACKED_FOREGROUND=)\d+',
        'VCS_MODIFIED_FOREGROUND': r'(typeset -g POWERLEVEL9K_VCS_MODIFIED_FOREGROUND=)\d+',
        'VCS_VISUAL_IDENTIFIER_COLOR': r'(typeset -g POWERLEVEL9K_VCS_VISUAL_IDENTIFIER_COLOR=)\d+',
        'VCS_LOADING_VISUAL_IDENTIFIER_COLOR': r'(typeset -g POWERLEVEL9K_VCS_LOADING_VISUAL_IDENTIFIER_COLOR=)\d+',
        'DIRENV_FOREGROUND': r'(typeset -g POWERLEVEL9K_DIRENV_FOREGROUND=)\d+',
        'PROMPT_CHAR_OK_FOREGROUND': r'(typeset -g POWERLEVEL9K_PROMPT_CHAR_OK_\{[^}]+\}_FOREGROUND=)\d+',
        'PROMPT_CHAR_ERROR_FOREGROUND': r'(typeset -g POWERLEVEL9K_PROMPT_CHAR_ERROR_\{[^}]+\}_FOREGROUND=)\d+',
        'TIME_FOREGROUND': r'(typeset -g POWERLEVEL9K_TIME_FOREGROUND=)\d+',
    }
    
    result = content
    
    for key, pattern in patterns.items():
        if key in color_mapping:
            replacement = f'\\g<1>{color_mapping[key]}'
            result = re.sub(pattern, replacement, result)
    
    if 'emoji' in color_mapping:
        emoji = color_mapping['emoji']
        emoji_pattern = r"(typeset -g POWERLEVEL9K_PROMPT_CHAR_\{[^}]+\}_[A-Z_]+CONTENT_EXPANSION=')[^']+(')"
        result = re.sub(emoji_pattern, f'\\g<1>{emoji}\\g<2>', result)

    git_formatter_patterns = {
        'GIT_CLEAN': (r"(local\s+clean='%)\d+(F')", 208),
        'GIT_MODIFIED': (r"(local\s+modified='%)\d+(F')", 214),
        'GIT_UNTRACKED': (r"(local\s+untracked='%)\d+(F')", 178),
        'GIT_CONFLICTED': (r"(local\s+conflicted='%)\d+(F')", 166),
        'GIT_META': (r"(local\s+meta='%)\d+(F')", 172),
    }
    
    for key, (pattern, default_color) in git_formatter_patterns.items():
        if key in color_mapping:
            new_color = color_mapping[key]
            result = re.sub(
                pattern.replace(r'\d+', str(default_color)),
                f'\\g<1>{new_color}\\g<2>',
                result
            )
    
    if 'GIT_META' in color_mapping:
        meta_color = color_mapping['GIT_META']
        else_pattern = r"(local\s+(?:meta|clean|modified|untracked|conflicted)='%)172(F')"
        result = re.sub(else_pattern, f'\\g<1>{meta_color}\\g<2>', result)
    
    return result


def create_p10k_file(color_template, template_file=None, output_file=None):

    if template_file is None:
        script_dir = Path(__file__).parent
        template_file = script_dir / 'custom-files' / 'orange-p10k.zsh'
    
    template_path = Path(template_file)
    
    if not template_path.exists():
        raise FileNotFoundError(f"Arquivo template não encontrado: {template_path}")
    
    if output_file is None:
        output_file = f'{color_template}-p10k.zsh'
    
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    color_mapping = get_color_mapping(color_template)
    
    updated_content = replace_colors_in_content(content, color_mapping)
    
    output_path = Path(output_file)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    return str(output_path)

