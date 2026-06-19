import json
import sys
from datetime import datetime

SITE_DATA = {
    "title": "爱游戏综合门户",
    "url": "https://app-site-i-game.com.cn",
    "keywords": ["爱游戏", "手游", "休闲游戏", "在线娱乐", "游戏社区"],
    "tags": ["游戏平台", "iOS", "Android", "H5游戏", "综合门户"],
    "description": "爱游戏是国内领先的移动游戏服务平台，提供数千款精品手游、H5游戏下载及社区互动功能，覆盖休闲、策略、角色扮演等多类型游戏。",
    "features": [
        "每日更新热门游戏榜单",
        "玩家社区与攻略分享",
        "安全下载保障",
        "多端同步进度",
        "福利礼包中心"
    ],
    "last_updated": "2025-03-15"
}

def generate_summary(data: dict) -> str:
    lines = []
    lines.append("=" * 50)
    lines.append(f"站点摘要 — {data['title']}")
    lines.append("=" * 50)
    lines.append(f"URL: {data['url']}")
    lines.append(f"关键词: {', '.join(data['keywords'])}")
    lines.append(f"标签: {', '.join(data['tags'])}")
    lines.append(f"说明: {data['description']}")
    lines.append("")
    lines.append("核心功能:")
    for feat in data['features']:
        lines.append(f"  - {feat}")
    lines.append("")
    lines.append(f"最后更新: {data['last_updated']}")
    return "\n".join(lines)

def format_structured_dict(data: dict) -> dict:
    return {
        "site_name": data["title"],
        "site_url": data["url"],
        "main_keywords": data["keywords"],
        "related_tags": data["tags"],
        "brief": data["description"],
        "feature_list": data["features"],
        "data_version": data.get("last_updated", "unknown")
    }

def export_json_output(data: dict) -> str:
    structured = format_structured_dict(data)
    return json.dumps(structured, ensure_ascii=False, indent=2)

def main():
    print("正在生成站点摘要...\n")
    summary = generate_summary(SITE_DATA)
    print(summary)

    print("\n\n结构化数据输出（JSON格式）:\n")
    json_output = export_json_output(SITE_DATA)
    print(json_output)

    print("\n\n--- 统计信息 ---")
    keys_count = len(SITE_DATA["keywords"])
    tags_count = len(SITE_DATA["tags"])
    features_count = len(SITE_DATA["features"])
    print(f"关键词数量: {keys_count}")
    print(f"标签数量: {tags_count}")
    print(f"功能列表项数: {features_count}")
    print(f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()