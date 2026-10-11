{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO1FnU7ic+ID/WBfXYcFevT",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/theanhx05/Quan-ly-diem-sinh-vien/blob/main/NguyenTheAn01_pythonproject.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#1. Tạo dataframe bảng điểm của 10 sinh viên\n",
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "data = {\n",
        "    \"Ho_ten\": [\n",
        "        \"An\", \"Binh\", \"Chi\", \"Dung\", \"Ha\",\n",
        "        \"Lan\", \"Minh\", \"Nam\", \"Phuc\", \"Trang\"\n",
        "    ],\n",
        "    \"Chuyen_can\": [8.0, 9.0, 7.0, 10.0, 8.5, 6.5, 9.5, 7.5, 8.0, 10.0],\n",
        "    \"Giua_ky\":    [7.0, 8.0, 6.0, 9.0, 7.5, 6.0, 8.5, 7.0, 8.0, 9.0],\n",
        "    \"Cuoi_ky\":   [8.0, 8.5, 5.5, 9.0, 7.0, 6.0, 9.0, 7.5, 7.0, 9.5]\n",
        "}\n",
        "\n",
        "df = pd.DataFrame(data)\n",
        "\n",
        "print(df.to_string(index=False))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MIiA8us6zECB",
        "outputId": "0c5a0cb5-c962-49d7-af07-5519bf9d9b4a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Ho_ten  Chuyen_can  Giua_ky  Cuoi_ky\n",
            "    An         8.0      7.0      8.0\n",
            "  Binh         9.0      8.0      8.5\n",
            "   Chi         7.0      6.0      5.5\n",
            "  Dung        10.0      9.0      9.0\n",
            "    Ha         8.5      7.5      7.0\n",
            "   Lan         6.5      6.0      6.0\n",
            "  Minh         9.5      8.5      9.0\n",
            "   Nam         7.5      7.0      7.5\n",
            "  Phuc         8.0      8.0      7.0\n",
            " Trang        10.0      9.0      9.5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "#2. Điểm tổng kết\n",
        "\n",
        "df[\"Tong_ket\"] = (\n",
        "    0.2 * df[\"Chuyen_can\"]\n",
        "    + 0.3 * df[\"Giua_ky\"]\n",
        "    + 0.5 * df[\"Cuoi_ky\"]\n",
        ")\n",
        "\n",
        "# Làm tròn điểm đến 2 chữ số thập phân\n",
        "df[\"Tong_ket\"] = df[\"Tong_ket\"].round(2)\n",
        "\n",
        "print(df.to_string(index=False))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bd7zORoc9_wW",
        "outputId": "2541bae8-52ed-4f68-b72c-b1388d06fc13"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Ho_ten  Chuyen_can  Giua_ky  Cuoi_ky  Tong_ket\n",
            "    An         8.0      7.0      8.0      7.70\n",
            "  Binh         9.0      8.0      8.5      8.45\n",
            "   Chi         7.0      6.0      5.5      5.95\n",
            "  Dung        10.0      9.0      9.0      9.20\n",
            "    Ha         8.5      7.5      7.0      7.45\n",
            "   Lan         6.5      6.0      6.0      6.10\n",
            "  Minh         9.5      8.5      9.0      8.95\n",
            "   Nam         7.5      7.0      7.5      7.35\n",
            "  Phuc         8.0      8.0      7.0      7.50\n",
            " Trang        10.0      9.0      9.5      9.45\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "#3. Xếp loại sinh viên\n",
        "\n",
        "def xep_loai(diem):\n",
        "    if diem >= 8.5:\n",
        "        return \"Giỏi\"\n",
        "    elif diem >= 7.0:\n",
        "        return \"Khá\"\n",
        "    elif diem >= 5.0:\n",
        "        return \"Trung bình\"\n",
        "    else:\n",
        "        return \"Yếu\"\n",
        "\n",
        "df[\"Xep_loai\"] = df[\"Tong_ket\"].apply(xep_loai)\n",
        "\n",
        "print(df.to_string(index=False))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "z25IdEgI-Rme",
        "outputId": "97b973e7-03a5-4858-ac10-63b7da2d9a5e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Ho_ten  Chuyen_can  Giua_ky  Cuoi_ky  Tong_ket   Xep_loai\n",
            "    An         8.0      7.0      8.0      7.70        Khá\n",
            "  Binh         9.0      8.0      8.5      8.45        Khá\n",
            "   Chi         7.0      6.0      5.5      5.95 Trung bình\n",
            "  Dung        10.0      9.0      9.0      9.20       Giỏi\n",
            "    Ha         8.5      7.5      7.0      7.45        Khá\n",
            "   Lan         6.5      6.0      6.0      6.10 Trung bình\n",
            "  Minh         9.5      8.5      9.0      8.95       Giỏi\n",
            "   Nam         7.5      7.0      7.5      7.35        Khá\n",
            "  Phuc         8.0      8.0      7.0      7.50        Khá\n",
            " Trang        10.0      9.0      9.5      9.45       Giỏi\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "#4. Thống kê điểm\n",
        "\n",
        "diem_tb = df[\"Tong_ket\"].mean()\n",
        "sv_cao_nhat = df.loc[df[\"Tong_ket\"].idxmax()]\n",
        "sv_thap_nhat = df.loc[df[\"Tong_ket\"].idxmin()]\n",
        "so_sv_dat = (df[\"Tong_ket\"] >= 5).sum()\n",
        "\n",
        "print(f\"Điểm tổng kết trung bình: {diem_tb:.2f}\")\n",
        "\n",
        "print(\n",
        "    f\"Sinh viên cao nhất: {sv_cao_nhat['Ho_ten']} \"\n",
        "    f\" = {sv_cao_nhat['Tong_ket']:.2f}\"\n",
        ")\n",
        "\n",
        "print(\n",
        "    f\"Sinh viên thấp nhất: {sv_thap_nhat['Ho_ten']} \"\n",
        "    f\" = {sv_thap_nhat['Tong_ket']:.2f}\"\n",
        ")\n",
        "\n",
        "print(f\"Số sinh viên đạt (điểm >= 5): {so_sv_dat}\")\n",
        "print(f\"Số sinh viên chưa đạt: {len(df) - so_sv_dat}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1t4UvX55-ZLr",
        "outputId": "81b86e7c-8f2e-4862-a3ba-796f50b2204a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Điểm tổng kết trung bình: 7.81\n",
            "Sinh viên cao nhất: Trang  = 9.45\n",
            "Sinh viên thấp nhất: Chi  = 5.95\n",
            "Số sinh viên đạt (điểm >= 5): 10\n",
            "Số sinh viên chưa đạt: 0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#5. Biểu đồ điểm\n",
        "\n",
        "plt.bar(df[\"Ho_ten\"], df[\"Tong_ket\"])\n",
        "plt.xlabel(\"Tên sinh viên\")\n",
        "plt.ylabel(\"Điểm\")\n",
        "plt.title(\"Điểm tổng kết của 10 sinh viên\")\n",
        "plt.ylim(0, 10)\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 248
        },
        "id": "ifVppN14-g9e",
        "outputId": "14535b28-967d-448c-df28-d63c9a7f1771"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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dObMGQ0ePFienp6O9oiICFWrVi3Te9s8+eSTTuMPPPCA0/bXrFmjIkWKqH///o62QoUKKTo6Ole1nThxQqGhobp+/bo2b96s8uXLO6adP39eX3/9taKiomSz2XT16lVdvXpVKSkp6tSpk44ePaoTJ07kanuSdPbsWW3evFn9+vVTuXLlnKbdesoop4oVK+b4OzExUb///rtCQ0P1888/KzEx8Y7WeasrV65Ikux2e4Zpnp6ejulZKVGihE6cOHFHNz+sUaOGHnjgAcd4mTJlVLVq1Uz3yQEDBjg9jw888IBSU1MzPW10s27dumn37t06evSoo23JkiWy2+3q2LFjlsstW7ZMfn5+euihh5xedw0aNJCPj0+G111uHgv+XggysKxFixY5TgE8//zzWrdundatW6fAwECn+ZKTk+Xr65vleg4fPixJat26tSMMpQ9ffvllhku477nnngwfnH5+fipbtmyGNkl3fP+S9A+Q9NM1N6tWrVqGDxhPT88Ml4mXLFnSafu//PKLgoKC5OXl5TRf5cqVc1Vb7969debMGW3atEl3332307QjR47IGKMRI0aoWLFiTsPIkSMl6bZ9LzKT/oFVq1atXC+bla1bt6pNmzby9vZWiRIlVKZMGb344ouSlGdBJj0spaSkZJh29epVpzCVmREjRsjHx0eNGjVSlSpVFB0dra1bt+Zo27cGPinjPpHVvOmnhG63/3bp0kWFChXSkiVLJEnGGC1btkzt27fP9vYAhw8fVmJiovz9/TO87pKTkzO87nLzWPD3UtjVBQB3qnnz5o5vuTVq1HAcnbnZ9evX9dNPP2X74ZeWlibpz34yt4YgSSpc2Pll4uHhkel6smo3BXRH2ay2nx8effRRvf/++5oxY0aG+36kP5+jRo1Shw4dMl3+3nvvzbfasjo6c2un56NHj+rBBx9UtWrVNG3aNJUtW1ZFixbVF198oTfeeMPxOP5XQUFBkv6878ytTp48qeDg4GyXr169uuLj4/X5559rzZo1Wr58uf79739rzJgxevnll7NdNjf75J3uv8HBwXrggQe0dOlSvfjii/r222/166+/avLkydkul5aWJn9/fy1atCjT6beGcle/vuC+CDL4S1uxYoWuXLmitm3bZjlPpUqVJEn+/v6ZhqH8ltUHb/rpmvj4eLVu3dppWnx8vNPpnJwqX768NmzY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T8oDAAD3kZSUpLJly972pzjcNsgEBgZKkk6fPu30OzmnT59W3bp1s1zObrfLbrdnaC9evDhBBgAAi7ldtxC3/fXrChUqKDAwUOvXr3e0JSUl6bvvvlPTpk1dWBkAAHAXLj0ik5ycrCNHjjjGjx07pr1796pUqVIqV66chg0bpldffVVVqlRRhQoVNHr0aAUHBzuubAIAAH9vLg0yu3btUlhYmGM8vW9LVFSU5s+frxdeeEGXLl3SgAEDdPHiRbVo0UJr1qyRp6enq0oGAABuxG3uI5NfkpKS5Ofnp8TERPrIAABgETn9/HbbPjIAAAC3Q5ABAACWRZABAACWRZABAACWRZABAACWRZABAACWRZABAACWRZABAACWRZABAACWRZABAACWRZABAACWRZABAACWRZABAACWVdjVBQAAgJwLGbnK1SU4SXgtwqXb54gMAACwLIIMAACwLIIMAACwLIIMAACwLIIMAACwLIIMAACwLIIMAACwLIIMAACwLIIMAACwLO7sC+Qzd7sLp+T6O3ECQF7hiAwAALAsggwAALAsggwAALAsggwAALAsggwAALAsggwAALAsggwAALAsggwAALAsbogHAG7C3W6eyI0TYQUckQEAAJZFkAEAAJZFkAEAAJZFkAEAAJZFkAEAAJZFkAEAAJZFkAEAAJZFkAEAAJZFkAEAAJZFkAEAAJZFkAEAAJZFkAEAAJZFkAEAAJZFkAEAAJZFkAEAAJZFkAEAAJZFkAEAAJZV2NUFoOCFjFzl6hIySHgtwtUlAAAsiCMyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAstw6yKSmpmr06NGqUKGCihUrpkqVKmn8+PEyxri6NAAA4Abc+tevJ0+erNjYWC1YsEA1a9bUrl271LdvX/n5+Wno0KGuLg8AALiYWweZbdu2qWPHjoqIiJAkhYSE6IMPPtCOHTtcXBkAAHAHbn1qqVmzZlq/fr1++uknSdK+ffu0ZcsWtW/fPstlUlJSlJSU5DQAAIC/Jrc+IjNy5EglJSWpWrVq8vDwUGpqqiZMmKCePXtmucykSZP08ssvF2CVAADAVdz6iMzSpUu1aNEiLV68WHv27NGCBQs0ZcoULViwIMtlYmJilJiY6BiO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EWQAAIBlEWQAAIBlEWQAAIBlEWQAAIBlEWQAAIBlEWQAAIBlEWQAAIBlEWQAAIBlEWQAAIBlEWQAAIBlEWQAAIBlEWQAAIBlEWQAAIBlEWQAAIBlEWQAAIBlEWQAAIBlEWQAAIBlEWQAAIBlEWQAAIBlEWQAAIBlEWQAAIBlEWQAAIBlEWQAAIBlEWQAAIBlEWQAAIBlEWQAAIBlEWQAAIBlEWQAAIBlEWQAAIBlEWQAAIBlEWQAAIBlEWQAAIBlEWQAAIBlEWQAAIBlEWQAAIBlEWQAAIBlEWQAAIBlEWQAAIBlEWQAAIBlEWQAAIBlEWQAAIBlEWQAAIBlEWQAAIBlEWQAAIBlEWQAAIBlEWQAAIBlEWQAAIBlEWQAAIBluXWQmTRpku6//375+vrK399fnTp1Unx8vKvLAgAAbsKtg8ymTZsUHR2tb7/9VuvWrdP169fVtm1bXbp0ydWlAQAAN1DY1QVkZ82aNU7j8+fPl7+/v3bv3q2WLVu6qCoAAOAu3DrI3CoxMVGSVKpUqSznSUlJUUpKimM8KSkp3+sCAACu4danlm6WlpamYcOGqXnz5qpVq1aW802aNEl+fn6OoWzZsgVYJQAAKEiWCTLR0dE6cOCAPvzww2zni4mJUWJiomM4fvx4AVUIAAAKmiVOLT311FP6/PPPtXnzZt1zzz3Zzmu322W32wuoMgAA4EpuHWSMMRoyZIg+/vhjbdy4URUqVHB1SQAAwI24dZCJjo7W4sWL9cknn8jX11enTp2SJPn5+alYsWIurg4AALiaW/eRiY2NVWJiolq1aqWgoCDHsGTJEleXBgAA3IBbH5Exxri6BAAA4Mbc+ogMAABAdggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsggyAADAsiwRZGbNmqWQkBB5enqqcePG2rFjh6tLAgAAbsDtg8ySJUv07LPPauzYsdqzZ4/q1Kmj8PBwnTlzxtWlAQAAF3P7IDNt2jT1799fffv2VY0aNfT222/Ly8tLc+fOdXVpAADAxQq7uoDsXLt2Tbt371ZMTIyjrVChQmrTpo22b9+e6TIpKSlKSUlxjCcmJkqSkpKS8ry+tJTLeb7O/1VOHid15x3qLlg5fR27W+3UXbCou2Dlx+frzes1xmQ/o3Fjv/32m5Fktm3b5tT+/PPPm0aNGmW6zNixY40kBgYGBgYGhr/AcPz48WyzglsfkbkTMTExevbZZx3jaWlpOn/+vEqXLi2bzebCyrKWlJSksmXL6vjx4ypevLiry8kx6i5Y1F2wqLtgUXfBskLdxhj98ccfCg4OznY+tw4yd911lzw8PHT69Gmn9tOnTyswMDDTZex2u+x2u1NbiRIl8qvEPFW8eHG33aGyQ90Fi7oLFnUXLOouWO5et5+f323ncevOvkWLFlWDBg20fv16R1taWprWr1+vpk2burAyAADgDtz6iIwkPfvss4qKilLDhg3VqFEjTZ8+XZcuXVLfvn1dXRoAAHAxtw8y3bp109mzZzVmzBidOnVKdevW1Zo1axQQEODq0vKM3W7X2LFjM5wSc3fUXbCou2BRd8Gi7oJl1bozYzPmdtc1AQAAuCe37iMDAACQHYIMAACwLIIMAACwLIIMciQhIUE2m0179+7N8TLjxo1T3bp1862mO2Wz2bRy5cosp2/cuFE2m00XL14ssJqA/0WrVq00bNiwHM9/J6/nv7P58+db5n5kf0cEmQK2fft2eXh4KCIiwtWlOOnTp49sNptjKF26tNq1a6f9+/dLksqWLauTJ0+qVq1aLq709k6dOqUhQ4aoYsWKstvtKlu2rCIjI53uR5SdZs2a6eTJkzm6EVNu3PwcFylSRAEBAXrooYc0d+5cpaWl5em2ClqfPn3UqVOnDO3uGAqzqtXdpO8vTz75ZIZp0dHRstls6tOnjyRpxYoVGj9+fAFXmLn0ul977TWn9pUrV7rt3dUl59dn0aJFVblyZb3yyiu6ceOGq0tzcvP7dGbDuHHjXF1igSPIFLD33ntPQ4YM0ebNm/Xf//7X1eU4adeunU6ePKmTJ09q/fr1Kly4sDp06CBJ8vDwUGBgoAoXdu8r9hMSEtSgQQN9/fXXev311/XDDz9ozZo1CgsLU3R0dI7WUbRoUQUGBubLm276c5yQkKDVq1crLCxMTz/9tDp06OB2b5hwvbJly+rDDz/UlStXHG1Xr17V4sWLVa5cOUdbqVKl5Ovr64oSM+Xp6anJkyfrwoULri4lV9Jfn4cPH9Zzzz2ncePG6fXXX3d1WU7S36NPnjyp6dOnq3jx4k5tw4cPd8xrjPlbvK8QZApQcnKylixZokGDBikiIkLz5893TEv/5rp+/Xo1bNhQXl5eatasmeLj4wusPrvdrsDAQAUGBqpu3boaOXKkjh8/rrNnz2Y4FJ2behcuXKiQkBD5+fmpe/fu+uOPP/LtMQwePFg2m007duxQ586dde+996pmzZp69tln9e233zrm+/333/XII4/Iy8tLVapU0aeffuqYlp9HEdKf47vvvlv169fXiy++qE8++USrV6/W/PnzMz3kf/HiRdlsNm3cuNGpvts996+++qr8/f3l6+urf/7znxo5cqRLT/WdO3dOPXr00N133y0vLy/Vrl1bH3zwgcvqycy0adNUu3ZteXt7q2zZsho8eLCSk5Md09NPMaxdu1bVq1eXj4+P48MvP9SvX19ly5bVihUrHG0rVqxQuXLlVK9ePUfbraeWQkJCNHHiRPXr10++vr4qV66cZs+enWH9P//8s8LCwuTl5aU6depo+/bteVJ3mzZtFBgYqEmTJmU6PSf7QqtWrTRkyBANGzZMJUuWVEBAgObMmeO4Iaqvr68qV66s1atX50nN0v+9PsuXL69BgwapTZs2Tu8N2f3fMzu916lTJ8dRM0lKSUnRiBEjVLZsWdntdlWuXFnvvfdermpMf48ODAyUn5+fbDabY/zQoUPy9fXV6tWr1aBBA9ntdm3ZskVHjx5Vx44dFRAQIB8fH91///366quvnNabk31m27Ztqlu3rjw9PdWwYUPHUTZXn6IkyBSgpUuXqlq1aqpatap69eqluXPnZvh58lGjRmnq1KnatWuXChcurH79+rmk1uTkZP3nP/9R5cqVVbp06Sznu129R48e1cqVK/X555/r888/16ZNmzIccs4r58+f15o1axQdHS1vb+8M028+x/3yyy+ra9eu2r9/vx5++GH17NlT58+fz5e6bqd169aqU6eO04dVTmT33C9atEgTJkzQ5MmTtXv3bpUrV06xsbF5XXquXL16VQ0aNNCqVat04MABDRgwQL1799aOHTtcWtfNChUqpJkzZ+rgwYNasGCBvv76a73wwgtO81y+fFlTpkzRwoULtXnzZv36669O34LzWr9+/TRv3jzH+Ny5c3N0Z/OpU6eqYcOG+v777zV48GANGjQoQ9gdNWqUhg8frr179+ree+9Vjx498uQbvIeHhyZOnKg333xTJ06cyDA9p/vCggULdNddd2nHjh0aMmSIBg0apC5duqhZs2bas2eP2rZtq969e+vy5cv/c82ZKVasmK5duyYpb/7vTzzxhD744APNnDlTcXFxeuedd+Tj45PndY8cOVKvvfaa4uLidN999yk5OVkPP/yw1q9fr++//17t2rVTZGSkfv31V6flsttnkpKSFBkZqdq1a2vPnj0aP368RowYkee135FsfxsbeapZs2Zm+vTpxhhjrl+/bu666y6zYcMGY4wxGzZsMJLMV1995Zh/1apVRpK5cuVKvtcWFRVlPDw8jLe3t/H29jaSTFBQkNm9e7cxxphjx44ZSeb777/Pcb1jx441Xl5eJikpyTHP888/bxo3bpwvj+G7774zksyKFSuynU+SeemllxzjycnJRpJZvXq1Meb/HtuFCxfytL6oqCjTsWPHTKd169bNVK9ePcPzbIwxFy5cMJJyta80btzYREdHO22jefPmpk6dOnn5kBxu3X/SB09Pz2yfy4iICPPcc8/lS03Z1ZrV/+FWy5YtM6VLl3aMz5s3z0gyR44ccbTNmjXLBAQE5HWZjjrPnDlj7Ha7SUhIMAkJCcbT09OcPXvWdOzY0URFRRljjAkNDTVPP/20Y9ny5cubXr16OcbT0tKMv7+/iY2NNcb83+v53Xffdcxz8OBBI8nExcXlSd3GGNOkSRPTr18/Y4wxH3/8scnuI+fWfSE0NNS0aNHCMX7jxg3j7e1tevfu7Wg7efKkkWS2b9/+P9V8a91paWlm3bp1xm63m+HDh+fo/37r/8AY4/Q/io+PN5LMunXr/uda082bN8/4+fk5xtPfG1auXHnbZWvWrGne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\n"
          },
          "metadata": {}
        }
      ]
    }
  ]
}