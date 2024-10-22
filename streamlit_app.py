import streamlit as st  

import pandas as pd  
import matplotlib.pyplot as plt  
import numpy as np  
import time

from datetime import datetime  
  
# 设定一些示例数据，你可以根据实际情况替换为自动生成或手动填写的数据  
report_number = "Report-001"  # 报告编号，可以手动输入或自动生成  
report_date = datetime.now().strftime("%Y-%m-%d")  # 报告日期，默认使用当前日期，也可手动填写  
document_name = "示例文档.pdf"  # 文档名称  
document_type = "PDF"  # 文档类型  
parsing_tool = "CustomParser 1.0"  # 解析工具  
analyst_name = "张三"  # 解析人员  
original_summary = """  
本文档主要探讨了人工智能在医疗领域的应用。首先，介绍了人工智能的基本概念和技术原理。  
接着，详细阐述了人工智能在医疗诊断、疾病预测、个性化治疗等方面的应用案例。  
此外，还讨论了人工智能在医疗领域面临的挑战和未来发展趋势。  
本文档强调了人工智能在提高医疗服务质量和效率方面的巨大潜力。  
"""  
tables = [
    ("表格1", [
        ["姓名", "年龄", "性别"],
        ["张三", 25, "男"],
        ["李四", 30, "女"]
    ]),
    ("表格2", [
        ["书名", "作者", "出版日期"],
        ["《Python编程》", "张三", "2023年"],
        ["《JavaScript编程》", "李四", "2022年"]
    ])
]
json_data = {"姓名": "张三", "年龄": 25, "性别": "男"}
# 假设你已经有了解析结果分析的内容，这里我们使用示例文本  
accuracy_analysis = """  
分析提取的数据与原文内容基本一致，但在某些数据点上存在差异。例如，原文中的某个日期被错误地提取为另一个日期，这可能是由于日期格式解析的问题导致的。  
"""  
  
completeness_analysis = """  
评估提取的数据相对完整，涵盖了文档中的大部分关键信息。然而，有少数关键数据点被遗漏，例如某个重要人物的姓名在提取结果中未出现，这可能是由于文本匹配算法未能准确识别导致的。  
"""  
  
efficiency_analysis = """  
解析过程的效率较高，解析速度较快，且自动化程度较高。然而，仍有改进空间，例如可以通过优化算法来进一步提高解析速度和准确性。  
"""  
  
other_issues = """  
在解析过程中遇到了一些问题，如文档格式复杂导致解析难度增加，以及数据格式不统一导致数据整合困难。为了解决这些问题，建议对文档进行预处理以统一格式，并优化解析算法以适应不同的文档结构。  
"""  

# 假设你已经有了结论和建议的内容，这里我们使用示例文本  
conclusion = """  
总结文档解析的结果，数据在准确性方面表现良好，大部分数据与原文内容一致，仅在少数数据点上存在差异。数据完整性方面，提取的数据涵盖了文档中的大部分关键信息，但仍有少数关键数据点被遗漏。解析效率方面，整体效率较高，但仍有优化空间。综合来看，本次文档解析达到了预期目标，但在数据准确性和完整性方面仍有待提升。  
"""  
  
recommendations = """  
根据解析结果分析，提出以下建议：
1) 改进解析工具中的日期格式解析算法，以提高数据准确性；
2) 优化文本匹配算法，以减少关键数据点的遗漏；
3) 进一步优化解析流程，提高解析效率。

这些建议的实施将有助于提升未来文档解析的质量和效率。  
"""  

with st.expander('预览文档解析报告', expanded=False) :
    container = st.container()
    # 创建一个Streamlit应用  
    container.header('文档解析报告概览')  
    container.markdown("""  
                    ---

    本报告是关于**{document_name}**的解析报告，由**{analyst_name}**于**{report_date}**完成。  

    ---

    """.format(document_name=document_name, analyst_name=analyst_name, report_date=report_date))


    container.header("报告信息")
    # 逐一展示各项报告信息  
    container.markdown(f"**报告编号**：{report_number}")  
    container.markdown(f"**报告日期**：{report_date}")  
    container.markdown(f"**文档名称**：{document_name}")  
    container.markdown(f"**文档类型**：{document_type}")  
    container.markdown(f"**解析工具**：{parsing_tool}")  
    container.markdown(f"**解析人员**：{analyst_name}")  

    container.header("一、文本内容概述")

    container.subheader("原文摘要")

    container.markdown(original_summary)


    container.subheader("二、表格内容展示")
    for title, table in tables:
        container.markdown(f"#### {title}")
        container.table(table)

    container.subheader("三、提取的JSON结构化数据")
    container.json(json_data)

    container.subheader("四、解析结果分析")
    
    # 展示数据准确性分析  
    container.subheader('数据准确性')  
    container.markdown(accuracy_analysis)  
    
    # 展示数据完整性分析  
    container.subheader('数据完整性')  
    container.markdown(completeness_analysis)  
    
    # 展示解析效率分析  
    container.subheader('解析效率')  
    container.markdown(efficiency_analysis)  
    
    # 展示其他问题  
    container.subheader('其他问题')  
    container.markdown(other_issues)  

    
    # 创建一个Streamlit应用  
    container.title('结论与建议')  
    
    # 展示结论  
    container.subheader('结论')  
    container.markdown(conclusion)  
    
    # 展示建议  
    container.subheader('建议')  
    container.markdown(recommendations)  
    
    # 报告结束及签名部分  
    container.subheader('报告结束')  
    container.markdown("""  
    ---  
    
    [报告编制人员签名]    
    _（请在此处手写或电子签名）_    
    
    
    [报告审核人员签名（如有需要）]    
    _（请在此处手写或电子签名，如果审核流程需要）_    

    ---
    """)  

    
with st.expander('数据分析可视化', expanded=False) :
    container = st.container()
    # 生成一些示例数据  
    np.random.seed(0)  
    data = pd.DataFrame({  
        'Category': ['A', 'B', 'C', 'D'],  
        'Values': np.random.randint(10, 100, size=4),  
        'Dates': pd.date_range(start='2023-01-01', periods=4, freq='M')  
    })  
    
    # 生成时间序列数据  
    # date_rng = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D', ) 
    # date_rng = map(lambda x: datetime(x, ), date_rng)
    date_rng = range(4)
    df = pd.DataFrame(date_rng, columns=['date'])  
    df['data'] = np.random.randn(len(df))  
    
    st.dataframe(data)
    # Streamlit布局  
    
    # 1. 条形图  
    st.subheader("条形图")  
    # bar_chart = data.plot(kind='bar', x='Category', y='Values', figsize=(10, 5))  
    fig, ax = plt.subplots()
    ax.bar(df['date'], df['data'])
    st.pyplot(fig)  
    
    # 2. 折线图（动态更新）  
    st.subheader("折线图（动态更新）")  
    slider = st.slider("选择日期范围", df['date'].min(), df['date'].max())
    filtered_df = df[df['date'] <= slider]  
    # line_chart = filtered_df.plot(kind='line', x='date', y='data', figsize=(10, 5))  
    fig, ax = plt.subplots()
    ax.plot(filtered_df['date'], filtered_df['data'])
    st.pyplot(fig)  
    
    # 3. 散点图（Plotly）  
    st.subheader("散点图（Plotly）")  
    fig, ax = plt.subplots()
    ax.scatter(df['date'], df['data'], )  
    ax.set_title('散点图示例')
    st.pyplot(fig)  
    
    # 4. 热力图（Seaborn）  
    st.subheader("热力图（Seaborn）")  
    # 生成一些随机数据用于热力图  
    fig, ax = plt.subplots()
    heatmap_data = np.random.rand(10, 12)  
    ax.imshow(heatmap_data, cmap='coolwarm')
    
    # 在方格上绘制数字
    for i in range(heatmap_data.shape[0]):  
        for j in range(heatmap_data.shape[1]):  
            ax.text(j, i, '{:.2f}'.format(heatmap_data[i, j]), ha='center', va='center', color='w')
    
    # heatmap = sns.heatmap(heatmap_data, annot=True, fmt=".2f", cmap='coolwarm')  
    # st.image(fig, caption='热力图示例', use_column_width=True)  
    st.pyplot(fig)
    
    # 5. 箱线图  
    fig, ax = plt.subplots()
    st.subheader("箱线图")  
    # boxplot = data.boxplot(column='Values', by='Category', figsize=(10, 5))  
    ax.boxplot(data['Values'],)
    st.pyplot(fig)  
    
    # 显示交互式元素  
    if st.button("刷新数据"):  
        data['Values'] = np.random.randint(10, 100, size=4)  
        fig, ax = plt.subplots()
            
        st.subheader("刷新后的条形图")  
        bar_chart_updated = data.plot(kind='bar', x='Category', y='Values', figsize=(10, 5))  
        st.pyplot(fig)

def draw(ax):
    
    # 仪表盘数据  
    value = 74  # 当前值  
    max_value = 100  # 最大值  
    
    # 创建仪表盘样式的圆形图  
    
    # 绘制背景圆  
    ax.fill_between(np.linspace(0, 2 * np.pi, 100), 0, 1, color='grey', alpha=0.25)  
    
    # 绘制当前值对应的圆弧  
    inds = np.linspace(0, value / max_value * 2 * np.pi, 100)  
    ax.plot(inds, np.ones_like(inds), color='blue', linewidth=2)  
    
    # 设置角度标签  
    ax.set_xticks(np.linspace(0, 2 * np.pi, 12, endpoint=False))  
    ax.set_xticklabels([])  # 隐藏标签，因为这里不需要  
    
    # 添加中心点和当前值文本  
    ax.plot(0, 0, "ko")  # 中心点  
    ax.text(0, 0, f'{value}%', horizontalalignment='center',
            verticalalignment='center',
            fontsize=14, color='red')  
    
    # 移除不必要的边框和轴标签  
    ax.spines['polar'].set_visible(False)  
    ax.set_yticklabels([])  
    ax.set_xticklabels([])  
    
with st.expander('饼图和仪表盘', expanded=False) :
    
    container = st.empty()
    labels = ['A', 'B', 'C', 'D']  
    sizes = np.random.randint(10, 100, size=4)

    # 绘制饼图  
    fig, ax = plt.subplots()  
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140,
        )  
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.  
    
    # 在Streamlit中显示图表  
    container.pyplot(fig)
    
    # fig, ax = plt.subplots(subplot_kw=dict(polar=True))
    # draw(ax)
    # container.pyplot(fig)
    
    time.sleep(0.1)