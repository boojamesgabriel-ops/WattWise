'use client'

import { useQuery } from 'convex/react'
import { api } from '../../convex/_generated/api'
import { useUser } from '@clerk/nextjs'
import { useRouter } from 'next/navigation'
import { useEffect } from 'react'
import Dashboard from '@/src/components/Dashboard'

export default function DashboardPage() {
  const { isSignedIn } = useUser()
  const router = useRouter()
  const appliances = useQuery(api.appliances.getUserAppliances)
  const budgets = useQuery(api.budgets.getBudget)

  useEffect(() => {
    if (!isSignedIn) {
      router.push('/')
    }
  }, [isSignedIn, router])

  if (!isSignedIn) {
    return null
  }

  const handleAddAppliance = (appliance: any) => {
    console.log('Add appliance:', appliance)
  }

  const handleRemoveAppliance = (id: string) => {
    console.log('Remove appliance:', id)
  }

  const handleClearAppliances = () => {
    console.log('Clear all appliances')
  }

  return (
    <Dashboard
      appliances={appliances || []}
      onAddAppliance={handleAddAppliance}
      onRemoveAppliance={handleRemoveAppliance}
      onClearAppliances={handleClearAppliances}
    />
  )
}
