"use node";
import { action } from "./_generated/server";
import { v } from "convex/values";
import { GoogleGenerativeAI } from "@google/generative-ai";

export const chat = action({
  args: { prompt: v.string() },
  handler: async (ctx, args) => {
    // 1. Get API key from Convex environment variables
    const apiKey = process.env.GEMINI_API_KEY;
    if (!apiKey) {
      throw new Error("GEMINI_API_KEY not set in Convex dashboard");
    }

    // 2. Initialize Gemini
    const genAI = new GoogleGenerativeAI(apiKey);
    const model = genAI.getGenerativeModel({ model: "gemini-3-flash" });

    // 3. Call Gemini
    const result = await model.generateContent(args.prompt);
    const response = await result.response;
    const text = response.text();

    return text;
  },
});
