import streamlit as st
import pandas as pd

# Mock data - replace with your actual data source
character_data = {
    "日": {
        "pinyin": "rì",
        "meaning": "sun, day",
        "etymology": "Pictograph of the sun",
        "structure": "像形字: 始见于甲骨文,是太阳的图形",
        "origins": {
            "oracle": "Oracle bone script: ☉",
            "seal": "Seal script: 日"
        },
        "related_chars": ["昌", "明", "晶", "時", "暗"],
        "words": ["今日", "日光", "日历", "星期日", "日出", "日落", "日期", "生日"],
        "idioms": ["日复一日", "日新月异", "日积月累", "日理万机", "日正当中"],
        "sentences": [
            "太阳每天从东方升起，西方落下。",
            "今日天气晴朗，适合外出。",
            "我们要珍惜时间，度过充实的每一天。",
            "日出时分，整个世界都被染成了金色。",
            "这个日历标记着所有重要的日期。"
        ],
        "poem": """
        望庐山瀑布 李白
        日照香炉生紫烟，
        遥看瀑布挂前川。
        飞流直下三千尺，
        疑是银河落九天。
        """,
    }
}

def main():
    st.set_page_config(layout="wide")
    st.title("Chinese Character Learning App")

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        search_term = st.text_input("Enter a character to search:")
        if search_term in character_data:
            display_character(search_term)
        else:
            st.write("Character not found. Try another search.")

def display_character(char):
    data = character_data[char]
    
    # Main character display
    st.header(f"{char}", anchor=False)
    st.subheader(f"{data['pinyin']} - {data['meaning']}")

    # Create three columns for the main content
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("字意解说", anchor=False)
        st.write(data['etymology'])

        st.subheader("字形构造", anchor=False)
        st.write(data['structure'])

        st.subheader("字源", anchor=False)
        for script, char in data['origins'].items():
            st.write(f"{script}: {char}")

    with col2:
        st.subheader("词组", anchor=False)
        st.write(", ".join(data['words']))

        st.subheader("成语", anchor=False)
        for idiom in data['idioms']:
            st.write(f"- {idiom}")

        st.subheader("行生字", anchor=False)
        st.write(", ".join(data['related_chars']))

    with col3:
        st.subheader("语句", anchor=False)
        for sentence in data['sentences']:
            st.write(f"- {sentence}")

    # Poem section (full width)
    st.subheader("诗词", anchor=False)
    st.text(data['poem'])

    # References section
    st.subheader("参考资料", anchor=False)
    st.write("- 百度汉语")
    st.write("- Hanzi Writer")
    st.write("- 第一学汉字")

    # Placeholder for visual components
    st.subheader("Visual Aids", anchor=False)
    st.write("(Placeholder for sun images and animations)")

if __name__ == "__main__":
    main()
