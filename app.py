col1, col2 = st.columns(2)

with col1:
    st.pyplot(plot_hist_price(model_df), use_container_width=False)

with col2:
    st.pyplot(plot_box_price(model_df), use_container_width=False)

col3, col4 = st.columns(2)

with col3:
    st.pyplot(
        plot_scatter(model_df, "ram_gb", "RAM, GB", "Залежність ціни від оперативної пам'яті"),
        use_container_width=False
    )

with col4:
    st.pyplot(
        plot_scatter(model_df, "storage_gb", "Storage, GB", "Залежність ціни від внутрішньої пам'яті"),
        use_container_width=False
    )

col5, _ = st.columns(2)

with col5:
    st.pyplot(
        plot_scatter(model_df, "fast_charging_w", "Fast charging, W", "Залежність ціни від швидкої зарядки"),
        use_container_width=False
    )
