import { mutation, query } from "./_generated/server";
import { getAuthUserId } from "@convex-dev/auth/server";

export const storeUser = mutation(async (ctx, args: { clerkId: string; email: string }) => {
  const userId = await getAuthUserId(ctx);

  if (!userId) {
    throw new Error("Not authenticated");
  }

  const existing = await ctx.db
    .query("users")
    .withIndex("by_clerkId", (q) => q.eq("clerkId", args.clerkId))
    .first();

  if (existing) {
    return existing._id;
  }

  return await ctx.db.insert("users", {
    clerkId: args.clerkId,
    email: args.email,
  });
});

export const getCurrentUser = query(async (ctx) => {
  const userId = await getAuthUserId(ctx);

  if (!userId) {
    return null;
  }

  return await ctx.db
    .query("users")
    .withIndex("by_clerkId", (q) => q.eq("clerkId", userId))
    .first();
});